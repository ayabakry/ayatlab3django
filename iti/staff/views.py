from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect,JsonResponse
from .models import *
from .forms import *
from myuser.models import myuser


# Create your views here.
def liststaff(request):
    context={}
    context['staffs']=Trainee.objects.all()
    return render (request,'liststaff.html',context)

def insertstaff(requset):
    context={}
    form=InsertTrainee()

    if(requset.method=='GET'):
        context['forms'] = form
        return render(requset, 'staff/insertstaff.html', context)
    else:
        form=InsertTrainee(requset.POST)
        if(form.is_valid()):
            mytraineer=Trainer.objects.get(id=requset.POST['trainer'])
            Trainee.objects.create(name=requset.POST['name'],nationalnum=requset.POST['nationalnum'],trainer=mytraineer)

        return HttpResponseRedirect(requset,'/staff/')

def insertuser(requset):
    context={}
    form=InsertUser()

    if(requset.method=='GET'):
        context['forms'] = form
        return render(requset, 'staff/insertuser.html', context)
    else:
        form=InsertUser(requset.POST)
        if(form.is_valid()):
            form.save()
        return HttpResponseRedirect(requset,'/staff')





# def stafflist(request):
#     return HttpResponse('List staff')
# def staffinsert(request):
#     return JsonResponse({'Name':'Ayat'})
# def staffupdate(request):
#     return JsonResponse({'Name':'Nadeen'})
# def staffdelete(request):
#     return HttpResponseRedirect('/listt')