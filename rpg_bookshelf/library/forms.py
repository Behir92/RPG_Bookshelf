from django import forms
from profiles.models import Profile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegisterProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def clean(self):
        cleaned_data = super().clean()
        raw_password = cleaned_data['password']
        cleaned_data['password'] = make_password(raw_password)
        return cleaned_data


class AuthForm(forms.Form):
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        login = cleaned_data['login']
        password = cleaned_data['password']
        user = authenticate(username=login, password=password)
        if user is None:
            raise forms.ValidationError("Błędny login lub hasło")
        cleaned_data['user'] = user
        return cleaned_data