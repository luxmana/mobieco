from django.urls import path
from . import views

urlpatterns = [
    path('my_garage/', views.autoparts_main, name='my_garage'),


]