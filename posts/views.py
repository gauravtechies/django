from django.shortcuts import render
from posts.models import Posts, PostsForm
# Create your views here.

def index(request):
    form = PostsForm()
    return render(request,'index.html',{'title': 'Add New Post','form':form})