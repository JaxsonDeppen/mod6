from django.db import models

# Create your models here.
class image(models.Model):
    img = models.ImageField(upload_to="images")