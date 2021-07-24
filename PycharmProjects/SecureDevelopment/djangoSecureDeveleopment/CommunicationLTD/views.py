from django.forms.fields import NullBooleanField
from django.shortcuts import render
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def home(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def forgotPassword(request):
    return render(request, 'forgot_password.html')
def changePassword(request):
    return render(request, 'forgot_password.html')


# Api user functions
def login(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            suerEmail = form.cleand_data.get('userEmail')
            messages.success(request,f'accunt login')
    else:
        form = UserChangeForm()
    return render(request,"login.html",{"form" : form })


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return NullBooleanField # need to change
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
