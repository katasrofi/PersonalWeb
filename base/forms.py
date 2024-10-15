from django.forms import ModelForm
from .models import Profiles 

class ProfilesForm(ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
