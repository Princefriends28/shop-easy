from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.models import User


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('login')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'An email has been sent to your email address')

    return render(request, 'accounts/register.html')