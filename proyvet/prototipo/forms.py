from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=75, label='Tu usuario')
    pwd = forms.CharField(max_length=75, type="password", label="Contraseña")

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=75, label="Nombre")
    apellido = forms.CharField(max_length=75, label="Apellido")
    domicilio = forms.CharField(max_length=75, label="Domicilio")
    telefono = forms.IntegerField(label="Telefono") # change for format phone
    email = forms.EmailField(max_length=254, label="E-mail")


