from django.db import models

class Address(models.Model):
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150, blank=True)
    postalCode = models.CharField(max_length=10)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

class Patient(models.Model):
    name = models.CharField(max_length=200)
    adm_date = models.DateTimeField('date published')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
