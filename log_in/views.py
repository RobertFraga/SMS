from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username'];
        password = request.POST['password'];
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('superadmin/')
        else:
            messages.success(request, ("invalid username or password, try again"))
            return redirect('/')      
    else:    
        return render(request, 'login/login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request ("you were logout"))
    return redirect('/')