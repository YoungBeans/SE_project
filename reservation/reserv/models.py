from login.models import User, Restaurant
from django.db import models

# Create your models here.

class Reservation(models.Model) :
    create_time = models.DateTimeField(auto_now=True)
    reservation_time = models.DateTimeField()
    people = models.IntegerField()
    acceptOn = models.BooleanField(default=False)

class relate_reserv(models.Model) :
    reservate = models.ForeignKey("Reservation", on_delete=models.CASCADE)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    class Meta :
        abstract = True