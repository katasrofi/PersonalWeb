from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='HOME'),
        path('profiles-general/', views.profiles, name='PROFILES'),
        path('profiles/<str:pk>/', views.ProfilesView.as_view(), name='PROFILES-DETAILS'),
        path('create-profiles/', views.CreateProfilesForm.as_view(), name='CREATE-PROFILES'),
        path('update-profiles/<str:pk>/', views.UpdateProfiles.as_view(), name='UPDATE-PROFILES'),
        ]
