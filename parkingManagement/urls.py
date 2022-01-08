from django.urls import path
from . import views

urlpatterns = [
    path('register/lot/',views.registerParkingLot, name='register-lot'),
]