from django.db import models

# Create your models here.
class Contact(models.Model):
    Firstname = models.CharField(max_length=100,null=True)
    Lastname = models.CharField(max_length=100,null=True)
    profilepicture =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True )
    username =models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)
    address2 =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    state =models.CharField(max_length=100,null=True)
    zip =models.CharField(max_length=100,null=True)
    
    
class Contact_1(models.Model):
    Firstname = models.CharField(max_length=100,null=True)
    Lastname = models.CharField(max_length=100,null=True)
    profilepicture =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,null=True )
    username =models.CharField(max_length=100,null=True)
    email =models.CharField(max_length=100,null=True)
    address =models.CharField(max_length=100,null=True)
    address2 =models.CharField(max_length=100,null=True)
    city =models.CharField(max_length=100,null=True)
    state =models.CharField(max_length=100,null=True)
    zip =models.CharField(max_length=100,null=True)