from django.db import models
from cloudinary.models import CloudinaryField

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = CloudinaryField('image')  # Cloudinary handles storage
