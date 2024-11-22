from django.shortcuts import render, redirect
from app8_authentication.forms import CustomRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User

#Email Verification namespace
import smtplib
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from .email_verification import verify_email 
from django.contrib.auth.decorators import login_required


def resend_verification_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        print(f"Checking email: {email}")  # Debugging statement

        try:
            # Try to fetch the user by email
            user = get_user_model().objects.get(email=email)
            print(f"User found: {user}")  # Debugging statement

            if user.is_active:
                # User exists and is active: Show message
                messages.info(request, "Already Register, login.")
            else:
                # User exists but not active: Resend verification email
                send_verification_email(request, user)
                messages.success(request, "A new verification link has been sent to your email.")
        except get_user_model().DoesNotExist:
            # Email does not exist in the database
            # This case should notify the user to register first
            messages.error(request, "This email is not registered. Please sign up first.")
    
    return redirect('login-app8')



def Invalid_Link(request):
    context={
        "sidebar_content": "Authentication Demo"
    }
    return render(request, "app8_authentication/invalid_link.html", context)



#After Registration ; This is landing page which gives button to go to gmailand see if verification link is sent to gmail or not
def VerifyEmailTemplate(request):
    context={
        "sidebar_content": "Authentication Demo"
    }
    return render(request,'app8_authentication/after-register-verify.html', context )



#On clicking Register Button ..This code is executed and sends verify link to GMAIL
def send_verification_email(user, request):
    uid = urlsafe_base64_encode(str(user.pk).encode())
    token = default_token_generator.make_token(user)
    verification_url = f"{request.scheme}://{request.get_host()}/app8/verify-email/{uid}/{token}/"

    html_message = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <h2 style="color: #4CAF50;">Please Verify Your Email</h2>
        <p>Click the link below to verify your email and activate your account:</p>
        <a href="{verification_url}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Verify Email</a>
    </body>
    </html>
    """

    sender_email = settings.EMAIL_HOST_USER
    recipient_email = user.email
    subject = "Verify Your Email"
    
    email_message = f"Subject: {subject}\n"
    email_message += "Content-Type: text/html\n\n"
    email_message += html_message

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, settings.EMAIL_HOST_PASSWORD)
            server.sendmail(sender_email, recipient_email, email_message)
        print("Verification email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def register(request):
    user_count = User.objects.count()
    register_form = CustomRegistrationForm()
    if user_count >=5:
        context={
            'message': '[User limit reached] | Remove Previously Registered Users"',
            'sidebar_content': 'Authentication Demo',
            'register_form': register_form,
        }
        return render(request, 'app8_authentication/register.html', context)

    if request.method == 'POST':
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.is_active = False  # Set user as inactive initially
            user.save()

            send_verification_email(user, request)
            return redirect('verify-email-app8')
    else:
        register_form = CustomRegistrationForm()

    context = {
        'register_form': register_form,
        'sidebar_content': 'Authentication Demo'
    }

    return render(request, 'app8_authentication/register.html', context)




#This code gets executed when user clicks verify email button on gmail
def verify_email_view(request, uidb64, token):
    return verify_email(request, uidb64, token)


def deleteUsers(request):
    # Delete all users except those who are admins (superusers)
    User.objects.exclude(is_superuser=True).delete()
    return redirect('register-app8') 


def LandingPage(request):
    context={
        "sidebar_content": "Authentication Demo"
    }
    return render(request, 'app8_authentication/landingpage.html', context)


@login_required
def afterLogin(request):
    context={
        "sidebar_content": "Authentication Demo"
    }
    return render(request, 'app8_authentication/afterlogin.html', context)    


''' 
without email varification registering
def register(request):
    register_form = None
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "New User Account Created, Login to get started!")
            return redirect('login-app8')
    else:
        register_form = CustomRegistrationForm()

    context = {
        'register_form': register_form,
        'sidebar_content': 'Authentication Demo'
    }
    return render(request, 'app8_authentication/register.html', context)
'''

#https://chatgpt.com/share/673f163c-9c78-800f-887b-9fdac05847a5