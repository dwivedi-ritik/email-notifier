from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 

from django.contrib import messages 

from .forms import  CustomUserCreationForm
from .models import Emails 


def home(request):
    if request.user.is_authenticated:
        return redirect('user-home')
    return render(request, 'index.html')


def sign_up(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            print(username , password)
            auth_user = authenticate(request , username=username , password=password)
            if auth_user is not None:
                login(request , auth_user)
                return redirect('user-home')

    return render(request , 'app/sign_up.html' , {'form':form})



@login_required(redirect_field_name='home')
def user_profile_home(request):
    if request.method == 'POST':
        try:
            email = Emails(title = request.POST['title'] ,description= request.POST['description'] ,  mail_text = request.POST['mail_text'] , \
                time = request.POST['time'] , status = False , author = request.user)
            email.save()
            print("email regisdted")
        except Exception:
            raise Exception
    emails_data = Emails.objects.filter(author=request.user)

    context = {
        "user_emails": emails_data,
    }

    return render(request, 'app/profile.html', context)


def login_user(request):
    context = {
        "alert":None
    }
    if request.method == 'POST':
        username = request.POST.get('usrname')
        password = request.POST.get('pass')

        auth_usr = authenticate(request , username=username , password=password)
        if auth_usr is None:
            context["alert"] = "Username or Password is incorrect"
            return render(request , 'app/login.html' , context)
        login(request, auth_usr)
        return redirect('user-home')
    else:
        return render(request, 'app/login.html' ,context )


def logout_user(request):
    logout(request)
    return redirect("home")
