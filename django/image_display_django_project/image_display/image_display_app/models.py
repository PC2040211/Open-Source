from django.db import models

# Create your models here.
class Image(models.Model):
    image_area=models.ImageField()
    def __str__ (self):
        return self.image_area