from django import forms
from .models import Dragon
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegistrationForm(UserCreationForm):
    class Meta:
        #imported django User from django.contrib.auth.models
        model = User
        # started with __all__ fields
        # fields = ('__all__')
        fields = ('first_name', 'last_name', 'email', 'username') #pass & confirmPass will always be present


class dragonForm(forms.ModelForm):
    name = forms.CharField(max_length=17, min_length=2, widget=forms.TextInput(attrs={"class": "form-control"}))
    # color = forms.CharField(max_length=12, min_length=3)
    class Meta:
        model = Dragon
        fields = ["name", "color", "hasMagic"]
        labels = {
            'color': 'Your Brilliant Color ',
            }
            