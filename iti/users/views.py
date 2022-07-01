from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
# from .forms import InsertTrainee,InsertUser
from myuser.models import myuser
from django.views.generic import ListView
# Create your views here.
from staff.views import insertuser

from staff.forms import InsertUser

from staff.models import Trainer


def listuser(request):
    ues=myuser.objects.all()
    context={}
    context['users']=ues
    return render(request,'listuser.html',context)


def Update(request,id):
    if(request.session.get('username') is not None):

        context = {}
        if (request.method == 'GET'):
            context['users']=myuser.objects.get(id=id)
            return render(request, 'update.html', context)
        else:
            myuser.objects.filter(id=id).update(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            return HttpResponseRedirect('/User/')
    else:
        return HttpResponseRedirect('/login')

def Delete(request,id):
    if (request.session.get('username') is not None):
        userdel=myuser.objects.filter(id=id).delete()
        return HttpResponseRedirect('/User/')
    else:
        return HttpResponseRedirect('/login')

class classbaseddelete(View):
    def get(self, request):
        context = {}
        form = InsertUser()
        context['forms'] = form
        return render(request, 'insertuser.html', context)
    def post(self, request):
            context = {}
            form = InsertUser()
            form = InsertUser(request.POST)
            if (form.is_valid()):
                form.save()
            return HttpResponseRedirect('/User')

class uppdateviews(ListView):
        model = Trainer
