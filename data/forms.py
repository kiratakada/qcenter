import os
import datetime

from cStringIO import StringIO
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.forms.util import ErrorList

from master.models import City

GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female')
)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'qcenter@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

class RegisterForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'qcenter@gmail.com'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'my password'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+62813999999'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'my address'}))

    image = forms.FileField(label="Image")
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="---")
