from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders_request, name='orders'),
    path('create_request/', views.createRequest, name='create_request'),
    path('purchase_update/<str:pk>/', views.purchase_update, name='purchase_update'),
    path('autoparts_main/', views.autoparts_main, name='autoparts_main'),


]