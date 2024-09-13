from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUser
from django.contrib import messages

# Create your views here.
def home(request):
    return HttpResponse("Working")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Redirect to the homepage after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def register_view(request):  
    if request.method == 'POST':
        form = CustomUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login.html')  
  # Redirect to the homepage after successful registration
    else:
        form = CustomUser()
    return render(request, 'register.html', {'form': form})