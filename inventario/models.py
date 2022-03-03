from django.db import models

# Create your models here.

class producto(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='zaiko_images')
    url=models.URLField(blank=True)