from django.urls import path
from . import views

urlpatterns = [
        path('', views.HomeView.as_view(), name='HOME'),
        path('profiles-general/', views.ProfilesList.as_view(), name='PROFILES'),
        path('profiles/<str:pk>/', views.ProfilesView.as_view(), name='PROFILES-DETAILS'),
        path('create-profiles/', views.CreateProfilesForm.as_view(), name='CREATE-PROFILES'),
        path('update-profiles/<str:pk>/', views.UpdateProfiles.as_view(), name='UPDATE-PROFILES'),
        path('delete-profiles/<str:pk>/', views.DeleteProfiles.as_view(), name='DELETE-PROFILES'),
        path('login/', views.CustomLoginPage.as_view(), name='LOGIN'),
        path('register/', views.CustomRegisterPage.as_view(), name='REGISTER'),
        path('logout/', views.CustomLogoutPage.as_view(), name='LOGOUT'),
        ]
