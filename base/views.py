from django.shortcuts import render
from .models import Product 
# Create your views here.

def home(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'base/home.html', context)

def profiles(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/profiles.html', context)


