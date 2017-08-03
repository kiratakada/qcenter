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

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self._user = None

    def get_user(self):
        return self._user

    def clean(self):
        if self.errors:
            return self.cleaned_data

        username = self.cleaned_data.get('username').strip()
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Password yang kamu masukkan salah, silahkan masukkan password yang benar.")
        if not user.is_active:
            raise forms.ValidationError("Akun kamu dalam masa ban")

        self._user = user

        return self.cleaned_data

class RegisterForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'XXXXX'}))
    firstname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'XXXXX'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+62 XXXXX'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'XXXXX'}))

    # image = forms.FileField(label="Image", required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label="---")


class ScheduleForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Apakah penyakit anda?'}), required=False)
    medicine_report = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Jenis obat yang pernah dipakai atau pantangan obat'}), required=False)
    trauma = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Gejala yang anda alami?'}), required=False)

