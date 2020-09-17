from django.shortcuts import render, redirect
from .models import *
from .forms import CreateRequestForm, PurchaseUpdateForm
from django.contrib.auth.decorators import login_required
from accounts.models import *
import uuid

def get_ref_code(): #generating order request reference code auto
    ref_code = str(uuid.uuid4())[:12].replace('-','').upper()
    try:
        code_exist = OrderRequest.objects.get(ref_code=ref_code)
        get_ref_code()
    except:
        return ref_code

@login_required(login_url='login')
def createRequest(request):
    form = CreateRequestForm(request.POST)
    if request.method =='POST':
        form = CreateRequestForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user.customer
            instance.ref_code = get_ref_code()
            instance.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request, 'commerce_autoparts/request_form.html', context)


def orders_request(request):
    orders_requests = OrderRequest.objects.all()
    return render(request, 'commerce_autoparts/orders_all.html', {'orders_requests': orders_requests})

def purchase_update(request,pk):
    cus_request = orderrequest.objects.get(id=pk)
    form = PurchaseUpdateForm()
    context = {
        'form':form
    }
    return render(request, 'commerce_autoparts/purchase_update.html', context)

def autoparts_main(request):
    return render(request, 'commerce_autoparts/autoparts_main.html')
