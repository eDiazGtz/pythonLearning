from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name"})) #placing field here will override the other field below.
    lastName = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"email@domain.com"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'firstName', 
            'lastName', 
            'email', 
            'password'
            ]
    def clean_firstName(self, *args, **kwargs): #django will clean the form upon save and django will add this validation in back-end
        firstName = self.cleaned_data.get("firstName")
        if "Hero " not in firstName:
            raise forms.ValidationError("First Name must contain Hero ")
        return firstName

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("gov"):
            raise forms.ValidationError("Please use Hyrule-assigned .gov Email")
        return email
            
class RawRegistrationForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name"})) #cannot do TextField --- only CharField
    lastName = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"email@domain.com"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirmPassword = forms.CharField(max_length=100,widget=forms.PasswordInput)

