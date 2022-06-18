from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def company(request):
    return render(request,'inventory_masters.html')

def stock_group_creation(request):
    return render(request,'stock_group_creation.html')