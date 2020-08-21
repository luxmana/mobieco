from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('account/', views.accountSettings, name='account'),
    path('mypage/', views.user_home, name='mypage'), # show general relevance topic to user
    path('my_dashboard/', views.my_dashboard, name='my_dashboard'), #ecommerce controller tools for autopars
    path('staff_dashboard/', views.staff_dashboard, name='staff_dashboard'),  # ecommerce controller tools for autopars
    path('customer/<str:pk>/', views.customer, name='customer'), #Provide customer purchases and other ecommerce related inpf

]