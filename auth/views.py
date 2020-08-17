from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                print('username already exists')
                return render(request, 'register.html', {"username": "username already exists"})
            elif User.objects.filter(email=email).exists():
                print('email already exists')
                return render(request, 'register.html', {"emailerror": "email already exists"})
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('pass do not match')
            return render(request, 'register.html', {"passerror": "passwords do not match"})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
