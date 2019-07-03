from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import  authenticate, login as authorize, logout as deauth
from django.contrib.auth.models import  User
# Create your views here.
def login(request):
    if(request.method=='POST'):
        form =AuthenticationForm()
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Username or password is not Correct')
            return redirect('/user/login')    
        else:
            authorize(request,user)
            return redirect('/user/profile')
    else:
        if(request.user.is_authenticated):
            return redirect('/user/profile')
        form=AuthenticationForm()
    return render(request,'user/login.html',{'title':'User Login','form':form})

def register(request):
    form =UserCreationForm
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'Account created successfully')
            return redirect('/user/login')
    return render(request,'user/register.html',{'title':'user Register', 'form':form})

def profile(request):
    if request.user.is_authenticated:
        return render(request,'user/profile.html',{'title':'Dashboard'})
    else:
        messages.info(request,'You need to login first')
        return redirect('/user/login')  

def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request,'You have been successfully Logged out')
        
    return redirect('/user/login')