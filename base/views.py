#from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProfilesForm 
# Create your views here.

class HomeView(ListView):
    model = Product
    template_name = 'base/home.html'
    context_object_name = 'product'
#    
#def home(request):
#    product = Product.objects.all()
#    context = {'product': product}
#    return render(request, 'base/home.html', context)
#
def profiles(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'base/profiles.html', context)

def CreateProfiles(request):
    form = ProfilesForm()
    if request.method == 'POST':
        form = ProfilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('HOME')

    context = {'form': form}
    return render(request, 'base/profiles_form.html', context)
