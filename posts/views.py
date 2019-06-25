from django.shortcuts import render
from posts.models import Posts, PostsForm
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    form = PostsForm()
    return render(request,'posts/index.html',{'title': 'Add New Post','forms':form})