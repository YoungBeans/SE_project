from django.db import models

# Create your models here.

class NormalUser(models.Model) :
    idName = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    nickName = models.CharField(max_length=10)
    def __self__(self) :
        return self.nickName

class User(NormalUser) :
    phoneNumber = models.CharField(max_length=12)
    location = models.ForeignKey("Location", on_delete=models.DO_NOTHING)
    isManager = models.BooleanField(default=False)

class Location(models.Model) :
    city = models.CharField(max_length=30)

class Restaurant(models.Model) :
    name = models.CharField(max_length=30)
    location = models.ForeignKey("Location", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)