''' 
#This also works but not beautiful forms
#------------------------------------
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
'''

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
            'placeholder': 'Enter your email address',
            'style': 'width: 100%; margin-bottom: 15px;'
        })
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
            'placeholder': 'Enter your password',
            'style': 'width: 100%; margin-bottom: 15px;'
        })
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={
            'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
            'placeholder': 'Confirm your password',
            'style': 'width: 100%; margin-bottom: 15px;'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
                'placeholder': 'Enter your username',
                'style': 'width: 100%; margin-bottom: 15px;'
            }),
        }




from django.contrib.auth.forms import PasswordResetForm
from django.utils.timezone import now
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        users = get_user_model().objects.filter(email=email)
        if not users.exists():
            raise ValidationError("No user is associated with this email.")
        
        # Allow only one reset per hour
        user = users.first()
        if user.last_login and (now() - user.last_login).seconds < 3:  # 3600 seconds = 1 hour
            raise ValidationError("You can request a password reset only once per hour.")
        
        return email

    def save(self, *args, **kwargs):
        kwargs['html_email_template_name'] = 'app8_authentication/password_reset_email.html'
        return super().save(*args, **kwargs)

