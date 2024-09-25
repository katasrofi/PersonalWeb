from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('HOME PAGE')

def profiles(request):
    return HttpResponse('PROFILES')


