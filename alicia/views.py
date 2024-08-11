from django.shortcuts import render

# Create your views here.
def HomeScreenView(request):
    return render(request, 'base.html', {})
