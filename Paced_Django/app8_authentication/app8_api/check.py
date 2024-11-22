# x.py

from django.contrib.auth import get_user_model

email = "sahaimbetter@gmail.com"

try:
    user = get_user_model().objects.get(email=email)
    if user.is_active:
        print("Already Registered, login.")
    else:
        print("User is not active. Resend verification email.")
except get_user_model().DoesNotExist:
    print("This email is not registered. Please sign up first.")
