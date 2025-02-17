
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User


from django.db import models

# Create your models here.
class imageOld(models.Model):
    img = models.ImageField(upload_to="images")


class ImageNew(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Image {self.id} uploaded by {self.user.username}"
class Comment(models.Model):
    image = models.ForeignKey(ImageNew, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username}"
