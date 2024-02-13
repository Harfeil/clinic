from django.contrib import admin
from .models import Patient

# Register your models here.

model_list = [Patient]
admin.site.register(model_list)