from django import forms
from .models import FileUploads, ImageUploads

# Using Django forms and then later on connecting to models in views
class FileUploadForm(forms.Form):
    file_upload = forms.FileField(required=True)

    # Manual Customization of styling
    labels = {
        "file_upload": "Choose File",  # Custom label for the file_upload field
    }

    widgets = {
        'file_upload': forms.FileInput(  # Corrected field name from 'name' to 'file_upload'
            attrs={
                'class': 'w3-monospace',  # You can keep if needed
            }
        )
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name in self.fields:
            if field_name in self.labels:
                self.fields[field_name].label = self.labels[field_name]
            if field_name in self.widgets:
                self.fields[field_name].widget = self.widgets[field_name]


# Directly connecting forms to models
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploads
        fields = "__all__"


        # Manual Customization of styling
        labels = {
            "image_upload": "Choose Image",  # Custom label for the file_upload field
        }
