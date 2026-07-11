from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(max_length=50, required=True, label="Nombre")
    last_name = forms.CharField(max_length=50, required=True, label="Apellido")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email'] 