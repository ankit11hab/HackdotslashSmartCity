from django.urls import path
from . import views

urlpatterns = [
    path('compain/',views.damageComplain, name='damage-complain'),
]