import django.forms as forms
from django.forms import ModelForm,forms
from .models import userlogin


class LoginForm(forms.Form):
    username = forms.CharField(max_length=35)
    password = forms.CharField(max_length=20)





