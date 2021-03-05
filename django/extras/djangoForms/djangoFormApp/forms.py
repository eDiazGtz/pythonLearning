from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    firstName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    confirm_password = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            'firstName',
            'lastName',
            'email',
        ]


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=17, widget=forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=100)


