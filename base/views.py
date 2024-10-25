from django.shortcuts import render#, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView 
from django.urls import reverse_lazy
from .models import Products
from .forms import ProfilesForm 
# Create your views here.

class HomeView(ListView):
    model = Products
    template_name = 'base/home.html'
    context_object_name = 'product'
    
#def home(request):
#    product = Products.objects.all()
#    context = {'product': product}
#    return render(request, 'base/home.html', context)

class ProfilesView(DetailView):
    model = Products
    template_name = 'base/profiles_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_profiles'] = Products.objects.all()
        return context 

def profiles(request):
    product = Products.objects.all()
    context = {'product': product}
    return render(request, 'base/profiles.html', context)

class CreateProfilesForm(CreateView):
    model = Products()
    template_name = 'base/profiles_form.html'
    form_class = ProfilesForm
    success_url = reverse_lazy('HOME')
#
#def CreateProfiles(request):
#    form = ProfilesForm()
#    if request.method == 'POST':
#        form = ProfilesForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('HOME')
#
#    context = {'form': form}
#    return render(request, 'base/profiles_form.html', context)

class UpdateProfiles(UpdateView):
    model = Products
    form_class = ProfilesForm
    template_name = 'base/profiles_form.html'
    context_object_name = 'form'
    success_url = reverse_lazy('HOME')
    pk_url_kwarg = 'pk'
