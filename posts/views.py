from django.shortcuts import render,redirect
from posts.models import Posts, PostsForm,Category
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    form = PostsForm()
    data = Posts.objects.all()
    categories =Category.objects.all()
    if request.method == 'POST':
        form=PostsForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/posts')
    return render(request,'posts/index.html',{'title': 'Add New Post','forms':form,'rows':data,'category':categories})