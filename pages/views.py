from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View 
from pages.models import About
# Create your views here.
#this is procedural view in this we have to use if else for get post
def home(request):
       return render(request,'pages/index.html',{'title':'Home page'})

def about(request):
    if(request.method =='GET' and request.GET.get('method')=='delete' and request.GET.get('id')):
            rec= About.objects.filter(id=request.GET.get('id'))
            rec.delete()
    if(request.method =='GET' and request.GET.get('method')=='edit' and request.GET.get('id')):
            rec= About.objects.filter(id=request.GET.get('id')).get()
            return render(request,'pages/edit.html',{'title':'About us','rows':rec})
    if(request.method=='POST'):
        if(request.GET.get('method')=="edit"):
            rec= About.objects.filter(id=request.GET.get('id'))
            rec.update(
                name=request.POST['name'],
                email=request.POST['email'],
                address=request.POST['address'],
                zipcode=request.POST['zipcode']
            )
            return HttpResponseRedirect('/pages/about/')
        else: 
            data= About(
                name=request.POST['name'],
                email=request.POST['email'],
                address=request.POST['address'],
                zipcode=request.POST['zipcode']
            )
            data.save()
        
        # email=request.POST['email']
        # address=request.POST['address'] 
        # zipcode=request.POST['zipcode']
        # return render(request,'about.html',{'title':'About us'})
    cnt=About.objects.all()
    return render(request,'pages/about.html',{'title':'About us','rows':cnt})

#this is class based view 
class contact(View):
    def get(self,request):
        return HttpResponse("<h1> Contact us </h1>")

def member(request,id):        
    return HttpResponse("<h1>Team member  id:{}</h1>".format(id)) 

def team(request):
    return HttpResponse("<h1>Team members</h1>")


def categoryWiseMember(request,cat_id,mem_id):
    return HttpResponse("<h1>Memberid: {} categoryid: {}</h1>".format(cat_id,mem_id))

#dynamic routes if cat_id and mem_id exist 
def greatmember(request):
    if(request.method=='GET' and 'cat_id' in request.GET and 'mem_id' in request.GET):
        return HttpResponse("<h1>Memberid: {} categoryid: {}</h1>".format(request.GET.get('mem_id'),request.GET.get('cat_id')))
    else:
        return HttpResponse("<h1>All Great members</h1>")