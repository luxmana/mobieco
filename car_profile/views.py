from django.shortcuts import render, redirect
from .models import *


def autoparts_main(request):
    return render(request, 'car_profile/my_garage.html')
