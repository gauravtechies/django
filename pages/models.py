from django.db import models

# Create your models here.
class About(models.Model):
    name= models.CharField(max_length=125, null=True)
    email= models.EmailField()
    address= models.CharField(max_length=255)
    zipcode = models.CharField(max_length=150)

    objects= models.Manager
