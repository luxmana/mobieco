from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders_request, name='orders'),
    path('create_request/', views.createRequest, name='create_request'),


]