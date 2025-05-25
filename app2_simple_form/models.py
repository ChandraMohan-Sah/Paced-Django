from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review_text = models.TextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]  # Ensure the rating is between 1 and 5
    )

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"




 

