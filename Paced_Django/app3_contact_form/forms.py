from django import forms 
from .models import ContactF



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactF
        fields = '__all__'

        #Manual Customization of styling
        labels = {
            "fullname":"Your Name",
            "email":"Email",
            "description":"Message"
        }

        error_messages = {
            "fullname": {
                "max_length":"Please enter a shorter name.",
                "required":"Your name must not be empty!"
            }
        }

        # Custom Widgets (with more styling and padding)
        widgets = {
            'fullname': forms.TextInput(
                attrs={
                    'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',  # You can keep if needed
                    'placeholder': 'Enter your full name',
                    'style': 'width: 100%; margin-bottom: 15px;'  
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
                    'placeholder': 'Enter your email address',
                    'style': 'width: 100%;margin-bottom: 15px;'  # Ensures the input takes full width
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
                    'placeholder': 'Say about your project requirement.',
                    'rows': 7,
                    'style': 'width: 100%; margin-bottom: 15px;'  # Ensures the textarea takes full width
                }
            ),
        }

