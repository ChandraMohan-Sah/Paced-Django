from django.shortcuts import render, redirect 
from app3_contact_form.forms import ContactForm

#smtp imports
import smtplib
from django.conf import settings

EMAIL_HOST_USER = settings.EMAIL_HOST_USER 
EMAIL_HOST_PASSWORD = settings.EMAIL_HOST_PASSWORD 

# --------Simple ContactForm : with smtp + nice formatiing--------#
def contactPOST(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Extract form data
                cleaned_data = form.cleaned_data
                subject = "New Contact Form Submission"
                html_message = f"""
                <html>
                <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                    <h2 style="color: #4CAF50;">New Submission</h2>
                    <p><strong>Full Name:</strong> {cleaned_data['fullname']}</p>
                    <p><strong>Contact Email:</strong> {cleaned_data['email']}</p>
                    <p><strong>Description:</strong></p>
                    <p style="white-space: pre-line; background-color: #f9f9f9; padding: 10px; border-radius: 5px; border: 1px solid #ddd;">
                        {cleaned_data['description']}
                    </p>
                </body>
                </html>
                """

                # Email setup
                sender_email = f"{EMAIL_HOST_USER}"
                recipient_email = "csah9628@gmail.com"
                password = f"{EMAIL_HOST_PASSWORD}"

                # Create email headers and body
                email_message = f"Subject: {subject}\n"
                email_message += "Content-Type: text/html\n\n"
                email_message += html_message

                # Send email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, recipient_email, email_message)

                print("HTML Email sent successfully!")

                # Save form and redirect
                # form.save()
                return redirect("thank-you-app3")
            except Exception as e:
                print(f"An error occurred: {e}")
    context={
        "form_data": ContactForm(),
        "sidebar_content" : "Contact Me [using SMTP]"
    }
    return render(request, "app3_contact_form/contact.html", context)




def ThankYou(request):
    context = {
        "sidebar_content": "Simple Form Demo",
        "content": "Your Form was Submitted to Owners Email using smtp service. Demonstration successfull 😊",
        "go_back": "contact-post"
    }
    return render(request, "thank-you.html", context)


