from django.db import models

class TableData(models.Model):
    animal = models.CharField(max_length=100)
    zoom_id = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.animal} ({self.zoom_id})"
