from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
# Create your views here.
#this is procedural view in this we have to use if else for get post
def home(request):
       return HttpResponse("<h1>Welcome to my django app</h1>")
def about(request):
    return HttpResponse("<h1>About us</h1>")
#this is class based view 
class contact(View):
    def get(self,request):
        return HttpResponse("<h1> Contact us </h1>")