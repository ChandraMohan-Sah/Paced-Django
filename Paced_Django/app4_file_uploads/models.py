from django.db import models

'''
    ----------------
    | README First |
    ----------------
    NOTE : Files are never stored in database rather.
    It's stored in Harddrive. Only location of that
    file is stored in the database. 

    File location are set using MEDIA in "settings.py" and "urls.py";
    It enables database to locate media file in project directory/harddrive
    --> So lets setup MEDIA now
'''

class FileUploads(models.Model):
    #Upload_to=""; Stores At root level; Not on app level
    file_upload = models.FileField(upload_to="file_upload")   #Location is : media_uploads/file_upload

 

class ImageUploads(models.Model):
    image_upload = models.ImageField(upload_to="image_upload")



 