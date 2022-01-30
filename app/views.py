from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import UserEmailForm , UserCreateForm
from .models import Emails 



def home(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username , email=email , password=password)
        #Login newly created user
        auth_user = authenticate(request , username= username , password=password)
        if auth_user is not None:
            login(request , auth_user)
            return redirect('user-home')
    else:
        return render(request , 'sign_up.html')


@login_required(redirect_field_name='home')
def user_profile_home(request):
    if request.method == 'POST':
        pass
    else:
        email_form = UserEmailForm()
        emails_data = Emails.objects.filter(author=request.user)
        print(list(emails_data))
        data = {
            "user":request.user,
            "email_form": email_form
        }

        return render(request , 'profile.html'  , data)
    

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('usrname')
        password = request.POST.get('pass')

        auth_usr = authenticate(request , username=username , password=password)
        if auth_usr is not None:
            login(request, auth_usr)

            return redirect('user-home')
        else:
            return HttpResponse("Invalid User Name and password")
    else:
        return render(request , 'login.html')


def logout_user(request):
    logout(request)
    return redirect("home")
