from django.db import models
from phone_field import PhoneField

# Create your models here.


class userSup(models.Model):
    fullName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    userName = models.CharField(max_length=50)
    passWord = models.CharField(max_length=100)
    phoneNumber = models.PositiveSmallIntegerField()
    profilePhoto = models.ImageField()
