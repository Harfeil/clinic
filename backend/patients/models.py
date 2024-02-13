from django.db import models

# Create your models here.

class Patient(models.Model):
    patientId = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    contactNum = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)