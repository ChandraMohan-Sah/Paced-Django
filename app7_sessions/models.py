from django.db import models

# Create your models here.

class SessionModel(models.Model):
    product = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.product}" 