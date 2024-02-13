from django.db import models

# Create your models here.

class Patient(models.Model):
    patientId = models.AutoField(primary_key = True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    ContactNum = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Role = models.CharField(max_length=100)
