from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Emails

class UserEmailForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Emails


class UserCreateForm(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()
    

