from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django import forms

# Create your models here.


class userSup(models.Model):
    fullName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    userName = models.CharField(max_length=50)
    passWord = models.CharField(max_length=100)
    phoneNumber = PhoneNumberField()
    profilePhoto = models.ImageField(
        upload_to="QANeiApp/templates/Image", blank=True)
