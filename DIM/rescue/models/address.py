from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Address(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    country = models.CharField(max_length=2, default='LU')
    postalcode = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)])
    city = models.CharField(max_length=150)
    tel = models.CharField(max_length=150)
    mail = models.CharField(max_length=150)

    class Meta:
        db_table = 'address'
        app_label = 'rescue'