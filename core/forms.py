from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nombreC = forms.CharField(label='Nombre Completo')
    telefono = forms.IntegerField(label='Telefono')
    direccion = forms.CharField(label='Direccion')
    ciudad = forms.CharField(label='Ciudad')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'nombreC', 'email', 'telefono', 'direccion', 'ciudad' ]
        help_texts = {k:"" for k in fields}