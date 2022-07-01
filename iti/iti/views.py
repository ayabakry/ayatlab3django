from django.shortcuts import render
from myuser.models import myuser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin,logout as authlogout

def index(request):
    if (request.session.get('username') is None and request.t.user.is_authenticated()):
         return render (request,'indexx.html')
    else:
        return render(request, 'login.html')


def login(request):
    #request.session.clear()
    if(request.session.get('username') is None):
        if (request.method == 'GET'):
            return render(request, 'login.html')
        else:
            myuserobject=myuser.objects.filter(username=request.POST['username'],password=request.POST['password'])
            authuserobject=authenticate(username=request.POST['username'],password=request.POST['password'])
            if(len(myuserobject)>0 and authuserobject is not None):
                request.session['username'] =myuserobject[0].username
                authlogin(request,authuserobject)
                return render(request, 'index.html')
            else:
                context = {}
                context['Erorr'] = 'invalid user.'
                return render(request, 'login.html', context)
    else:
        return  render(request,'indexx.html')

def register(request):
    if(request.method=='GET'):
        return render(request,'register.html')
    else:
        print(request.POST)

        u=myuser(username=request.POST['username'])
        u.email=request.POST['email']
        u.password=request.POST['password']
        u.save()
        User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'],is_superuser=True,is_staff=True)
        return render(request,'login.html')


def logout(request):
    if (request.session.get('username') is None and request.t.user.is_authenticated()):
        request.session.clear()
        authlogout(request,request.user)
    return render(request,'indexx.html')
