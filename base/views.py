from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from django.views.generic.edit import FormView 
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.db.models import Q 
from django.urls import reverse_lazy
from .models import Products
from .forms import ProfilesForm, RegisterForm  
# Create your views here.

class HomeView(ListView):
    model = Products
    template_name = 'base/home.html'
    context_object_name = 'product'

    def get_queryset(self):
        q = self.request.GET.get('q')

        if q:
            return Products.objects.filter(
                    Q(name__icontains=q) |
                    Q(work_experience__icontains=q) |
                    Q(skills__icontains=q) | 
                    Q(portfolio__icontains=q) |
                    Q(testimoni__icontains=q) 
                    )
        else:
            return Products.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Save the item into list 
        context['sidebar_product'] = Products.objects.all()
        
        # Count the search result
        q = self.request.GET.get('q')

        if q:
            context['search_count'] = self.get_queryset().count()
        else:
            context['search_count'] = Products.objects.all().count()

        # Return the result 
        return context 

#def home(request):
#    product = Products.objects.all()
#    context = {'product': product}
#    return render(request, 'base/home.html', context)
class CustomLoginPage(LoginView):
    template_name = 'login_register.html'
    redirect_authenticated_user = True 

    def form_valid(self, form):
        username = self.request.POST.get('username').lower()
        password = self.request.POST.get('password')

        # Authenticate user 
        user = authenticate(self.request, 
                            username=username,
                            password=password)
        
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'You Have Successfully Login')
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def form_invalid(self, form):
        username = self.request.POST.get('username')

        # Check account exist or not 
        if not get_user_model().objects.filter(username=username).exists():
            messages.error(self.request, "Account doesn't exist")
        else:
            messages.error(self.request, 'Wrong password')

        return super().form_invalid(form)
    
    def get_success_url(self):
        return reverse_lazy('HOME')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = 'login'
        return context 
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('HOME')
        return super().dispatch(request, *args, **kwargs)

class CustomLogoutPage(LogoutView):
    next_page = reverse_lazy('HOME')

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, "You Have Successfully Logged Out")
        return super().dispatch(request, *args, **kwargs)

class CustomRegisterPage(FormView):
   template_name = 'login_register.html'
   form_class = RegisterForm 
   success_url = reverse_lazy('HOME')

   def form_valid(self, form):
       # Save the account and adjust the name into lowercase
       user = form.save(commit=false)
       user.username = user.username.lower()
       user.save()

       # Login the account and redirect to home page 
       login(self.request, user)
       messages.success(self.request, 'Registration Successfully')
       return super().form_valid(form)
   
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

class CreateProfilesForm(LoginRequiredMixin, CreateView):
    model = Products 
    template_name = 'base/profiles_form.html'
    form_class = ProfilesForm
    success_url = reverse_lazy('HOME')
    login_url = 'LOGIN'

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

# Edit current profiles 
class UpdateProfiles(LoginRequiredMixin, UpdateView):
    model = Products
    form_class = ProfilesForm
    template_name = 'base/profiles_form.html'
    context_object_name = 'form'
    success_url = reverse_lazy('HOME')
    pk_url_kwarg = 'pk'
    login_url = 'LOGIN'
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(self.login_url)

        profile = self.get_object()

        if request.user != profile.user:
            return HttpResponse('You are not allowed here')

        return super().dispatch(request, *args, **kwargs)
# Delete Profiles 
class DeleteProfiles(LoginRequiredMixin, DeleteView):
    model = Products
    template_name = 'base/delete.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('HOME')
    #pk_url_kwarg = 'pk'
    login_url = 'LOGIN'
