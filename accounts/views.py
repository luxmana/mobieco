from django.shortcuts import render, redirect
from commerce_autoparts.models import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Customer


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form =CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username', 'email')
                Customer.objects.create(
                    username=user,
                    name=user.username,
                    email=user.email
                )
                messages.success(request,'account was created for '+ username)
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR Password is incorrect')

        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)

login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)


login_required(login_url='login')
def user_home(request):
    return render(request, 'accounts/mypage.html')


login_required(login_url='login')
def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.orderrequest_set.all() #not finalize...error
    context = {'customer': customer, 'orders': orders}
    return render(request,'accounts/customer.html', context)

login_required(login_url='login')
def my_dashboard(request):
    my_orders = OrderRequest.objects.filter(user=request.user.customer)
    total_requests = my_orders.count()
    drafts = my_orders.filter(draft=True).count()

    context = {
        'my_orders': my_orders,
        'total_requests' : total_requests,
        'drafts' : drafts
    }
    return render(request, 'accounts/my_dashboard.html', context)

login_required(login_url='login')
def staff_dashboard(request):
    orders_requests = OrderRequest.objects.all()
    return render(request, 'accounts/staff_dashboard.html', {'orders_requests': orders_requests})
