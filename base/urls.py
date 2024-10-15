from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='HOME'),
        path('profiles/<str:pk>/', views.profiles, name='PROFILES'),
        path('create-profiles/', views.CreateProfiles, name='CREATE-PROFILES'),
        ]
