from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else: # si se accede mediante el metodo GET
        form = UserRegisterForm()
        
    context = { 'form' : form }
    return render(request, 'register.html', context)

def profile(request):
    return render(request, 'profile.html')
