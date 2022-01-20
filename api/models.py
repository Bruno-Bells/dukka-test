from pyexpat import model
from django.db import models

# Create your models here.

Service_choices = (
    ("Electricity bill", "Electricity bill"),
    ("Water bill", "Water Bill"),
    ("Refuse Fee", "Refuse Fee")
)

class Receipt(models.Model):
    full_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=15)
    Services = models.CharField( max_length=100)
    totalAmount = models.CharField(max_length=100)

