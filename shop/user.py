from django.core.checks import messages
from django.forms import forms
from django.http import request
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_list_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save_user()
            return redirect ('index')
    return render (
        request = request,
        template_name= ('user/register.html'),
        context={
            'form':form
        }

    )

def login_user(request):
    # form = LoginForm()
    message = ""
    if request.method=="POST":
        # form=LoginForm(request.POST)
        # if form.is_valid():
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user:
            login(request,user) # Giữ đang nhập khi user correct
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return redirect ('index')
        else:
            message= "Input information is incorrect"
    return render(
        request=request,
        template_name=('user/login.html'),
        context={
            # 'form':form,
            'message': message
        }
    )
