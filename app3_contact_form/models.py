from django.db import models

# Create your models here.
class ContactF(models.Model):
    fullname = models.CharField(max_length =60)
    email = models.EmailField(max_length = 50)
    description = models.TextField() 

    def __str__(self):
        return f"{self.fullname} - {self.email}"

        
