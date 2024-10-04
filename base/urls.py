from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='HOME'),
        path('profiles/<str:pk>/', views.profiles, name='PROFILES')
        ]
