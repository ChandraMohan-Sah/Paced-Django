from django import forms 
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        #Manual Customization of styling
        labels = {
            "name":"Your Name",
            "email":"Email",
            "review_text":"Review Description",
            "rating":"Rating"
        }

        error_messages = {
            "name": {
                "max_length":"Please enter a shorter name.",
                "required":"Your name must not be empty!"
            }
        }

        # Custom Widgets (with more styling and padding)
        widgets = {
            'name': forms.TextInput(
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
            'review_text': forms.Textarea(
                attrs={
                    'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
                    'placeholder': 'Say about your project requirement.',
                    'rows': 7,
                    'style': 'width: 100%; margin-bottom: 15px;'  # Ensures the textarea takes full width
                }
            ),
            'rating': forms.NumberInput(
                attrs={
                    'class': 'w3-input w3-border w3-border-blue w3-round-large w3-small',
                    'style': 'width: 100%; margin-bottom: 15px;',  
                    'min': 1,  
                    'max': 5, 
                }
            )
        }








