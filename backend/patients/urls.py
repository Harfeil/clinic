from django.contrib import admin
from django.urls import path
from .views import PatientView

urlpatterns = [
    path('patients/', PatientView.as_view()),
]
