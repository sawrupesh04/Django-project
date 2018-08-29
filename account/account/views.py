from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "index.html", context)

def signup(request):
    if request.method == 'POST':
        # user has info and want to sign up
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'User name already exits.Try again with different username'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('index')
        else:
            return render(request, 'signup.html', {'error': 'password must match!'})


    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Username or password incorrect!'})

    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login.html', {'message': 'Logged out!'})
