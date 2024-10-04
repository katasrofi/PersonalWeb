from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def profiles(request, pk):
    return render(request, 'base/profiles.html')


