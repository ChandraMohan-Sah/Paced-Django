from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponseRedirect

from app4_file_uploads.forms import FileUploadForm, ImageUploadForm
from app4_file_uploads.models import FileUploads, ImageUploads


class CreateUploadView(View):
    def get(self, request):
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
        if image_saved or file_saved:
            return redirect("thank-you-app4")

        # If neither form is valid, re-render the page with errors
        context = {
            "image_form": image_form,
            "file_form": file_form,
            "sidebar_content": "File Upload Demo",
        }
        return render(request, "app4_file_uploads/file_upload.html", context)











#-------------2. Django Helper Function for Upload Feature ------------------

'''
class CreateImageUploadView(View):
    def get(self, request):
        form = ImageUploadForm()
        context ={
            "sidebar_content": "File Upload Demo",
            "form_data2":form
        }
        return render(request, "app4_file_uploads/file_upload.html", context)



    def post(self, request):
        submitted_data = ImageUploadForm(request.POST, request.FILES)

        if submitted_data.is_valid():
            uploaded_image = request.FILES["image_upload"]

            # Save the file to the database
            uploaded_data = ImageUploads(image_upload=uploaded_image)
            uploaded_data.save()
            return redirect("thank-you-app4")
        else:
            print("Form is not valid. Errors:", submitted_data.errors)

        context ={
            "form_data2":submitted_data,
            "sidebar_content": "File Upload Demo"
        }
        return render(request, "app4_file_uploads/file_upload.html", context)
        

class CreateFileUploadView(View):
    def get(self, request):
        form = FileUploadForm()
        context ={
            "sidebar_content": "File Upload Demo",
            "form_data1":form
        }
        return render(request, "app4_file_uploads/file_upload.html", context)



    def post(self, request):
        submitted_data = FileUploadForm(request.POST, request.FILES)

        if submitted_data.is_valid():
            uploaded_file = request.FILES["file_upload"]

            # Save the file to the database
            uploaded_data = FileUploads(file_upload=uploaded_file)
            uploaded_data.save()
            return redirect("thank-you-app4")
        else:
            print("Form is not valid. Errors:", submitted_data.errors)

        context ={
            "form_data1":submitted_data,
            "sidebar_content": "File Upload Demo"
        }
        return render(request, "app4_file_uploads/file_upload.html", context)
        
'''

#----------------------------------------------------------------












#--------------1. Custom File Upload Logic----------------------

#     1.Why Use file.chunks()?
#     =>Uploads can be large; chunking prevents the server from running out of memory.

#     2.Hardcoded Path (temp/filename.jpg): [save location; only saves file with .jpg extension]

#     3.wb+ means write binary mode:
#         w: Opens the file for writing (creates or overwrites it).
#         b: Binary mode (handles file as raw bytes, not text).
#         +: Allows both reading and writing.

'''
# For Storing Uploaded .jpg  file in a file structure
def store_file(file):
    with open("temp/filename.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


#Funtion handling get and post request 
class CreateFileUploadView(View):
    def get(self, request):
        context ={
            "sidebar_content": "File Upload Demo"
        }
        return render(request, "app4_file_uploads/file_upload_manual.html", context)
        
    def post(self, request):
        # print(request.FILES["fileUpload"])   #fileUpload is a variable in frontent name="fileUpload"
        store_file(request.FILES["fileUpload"])
        return HttpResponseRedirect("thank-you-page-app4/")

'''
#----------------------------------------------------------------


#Thank-You Page
def ThankYou(request):
    context = {
        "sidebar_content": "File Upload Demo",
        "content": "Your data was stored in Harddisk [note: not on database]. Demonstration successfull 😊",
        "go_back": "upload-app4"
    }
    return render(request, "thank-you.html", context)
