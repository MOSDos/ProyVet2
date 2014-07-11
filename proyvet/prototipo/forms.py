# -*- encoding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from PIL import Image as PImage
from models import *
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class CreateSuperUserFrom(UserCreationForm):
   class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        permissions = (
           ("can_jugar", "Can Jugar"),
           )

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'domicilio', 'telefono', 'email']
