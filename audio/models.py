from django.db import models

# Create your models here.

# models.py
from django.db import models

class ImageUpload(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # images/ is the directory where images will be saved
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DemoMCall(models.Model):

    audio = models.FileField( upload_to =  'upload_audio/')


