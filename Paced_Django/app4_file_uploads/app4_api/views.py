from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect

from app4_file_uploads.forms import FileUploadForm, ImageUploadForm
from app4_file_uploads.models import FileUploads, ImageUploads


class CreateUploadView(View):
    def get(self, request):
        #fetching forms
        image_form = ImageUploadForm()
        file_form = FileUploadForm()

        context = {
            "sidebar_content": "File Upload Demo",
            "image_form": image_form,
            "file_form": file_form,
        }
        return render(request, "app4_file_uploads/file_upload.html", context)


    def post(self, request):
        image_form = ImageUploadForm(request.POST, request.FILES)
        file_form = FileUploadForm(request.POST, request.FILES)

        # Flags to track if the forms are valid
        image_saved = False
        file_saved = False

        #Count Objects in database first
        if ImageUploads.objects.count() >=4 or FileUploads.objects.count() >= 4:
            message = "Database Full -First Delete Previous files and images"
            image_form = ImageUploadForm()
            file_form = FileUploadForm()

            context = {
                "sidebar_content": "File Upload Demo",
                "message": message,
                "image_form": image_form,
                "file_form": file_form
            }
            return render(request, "app4_file_uploads/file_upload.html", context)

        # Check and save the image form
        if "image_upload" in request.FILES:
            if image_form.is_valid():
                uploaded_image = request.FILES["image_upload"]
                ImageUploads.objects.create(image_upload=uploaded_image)
                image_saved = True
            else:
                print("Image Form is not valid. Errors:", image_form.errors)

        # Check and save the file form
        if "file_upload" in request.FILES:
            if file_form.is_valid():
                uploaded_file = request.FILES["file_upload"]
                FileUploads.objects.create(file_upload=uploaded_file)
                file_saved = True
            else:
                print("File Form is not valid. Errors:", file_form.errors)

        # Redirect if at least one form was successfully saved
        if image_saved and file_saved:
            return redirect("thank-you-app4")
    

        context = {
            "image_form": image_form,
            "file_form": file_form,
            "sidebar_content": "File Upload Demo"
        }
        return render(request, "app4_file_uploads/file_upload.html", context)


def DeleteImages_and_Files(request):
    ImageUploads.objects.all().delete()
    FileUploads.objects.all().delete()
    return redirect("upload-app4")


#Thank-You Page
def ThankYou(request):
    #fetching the uploaded files from database
    images = ImageUploads.objects.all()
    files = FileUploads.objects.all()

    context = {
        "sidebar_content": "File Upload Demo",
        "content": "Your data was stored in Harddisk [note: not on database]. Demonstration successfull 😊",
        "go_back": "upload-app4",
        "images":images,
        "files":files
    }
    return render(request, "app4_file_uploads/thank-you-app4.html", context)
