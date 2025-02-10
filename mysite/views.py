from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout

# Home view (only accessible after login)
@login_required
def home(request):
    context = {'greeting': 'Hello, welcome to the Attendance System!'}
    return render(request, 'home.html', context)

# Registration view (optional)
def register_view(request):
    # Implement your register logic here
    return render(request, 'register.html')
