from django.shortcuts import render
from django.http import HttpResponse
from FIRSTAPPLICATION.models import *
from FIRSTAPPLICATION.custform import *

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")

def index1(request):
    frm = CustomerForm()
    if request.method == "POST":
        formdata = CustomerForm(request.POST)
        if formdata.is_valid():
            namef = formdata.cleaned_data['name']
            custdata = Customer.objects.filter(name=namef).values()
            return render(request, 'FIRSTAPPLICATION/customers.html', context={'custdata':custdata})
    return render(request, 'FIRSTAPPLICATION/index.html', context={'form':frm})

def customers(request):
    cust1 = Customer.objects.all()
    return render(request, 'FIRSTAPPLICATION/customers.html', context={'custdata':cust1})

def vieworders(request):
    orders = orderhist.objects.all()
    return render(request, 'FIRSTAPPLICATION/orderhistory.html', context={'orders':orders})