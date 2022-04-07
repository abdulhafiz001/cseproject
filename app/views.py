from django.shortcuts import render
from django.http import HttpResponse

from app.models import Cars 

# Create your views here.


def index(request):
    carsHome = Cars.objects.all()[:9]
    context = {
        "cars":carsHome,
    }
    return render(request, 'index.html', context)
    

def About(request):
    return render(request, 'About.html')


def propage(request):
    return render(request, 'propage.html')

def pro2(request):
    return render(request, 'pro2.html')

def pro3(request):
    return render(request, 'pro3.html') 

def account(request):
    return render(request, 'account.html')

def shop(request):
    return render(request, 'shop.html')

def pro(request):
    return render(request, 'pro.html')

def pro4(request):
    return render(request, 'pro4.html')  
