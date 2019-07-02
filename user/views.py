from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def login(request):
    form =AuthenticationForm()
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