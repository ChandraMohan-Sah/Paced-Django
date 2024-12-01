from django.db import models

# Create your models here.

class SessionModel(models.Model):
    product = models.CharField(max_length=70, default="xyz")
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product}-{self.quantity}"