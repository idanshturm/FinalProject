from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'login.html')


def sign(request):
    return render(request, 'signup.html')

def changePassword(request):
    return render(request, 'change_password.html')