# -*- encoding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from PIL import Image as PImage
from models import *

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        } 
        