from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model, login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.shortcuts import redirect
from django.contrib import messages

def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(request, "Email verified! You can now login 🐒.")
            return redirect('login-app8')
        else:
            messages.error(request, "This Link has been expired.")
            return redirect('invalid-link')
    except Exception:
        messages.error(request, "Invalid link.")
    return redirect('login-app8')

