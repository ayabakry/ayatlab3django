"""iti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from student.views import *
from staff.views import *
from reports.views import *
from iti.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('list', studentlist),
    # path('insert', studentinsert),
    # path('update', studentupdate),
    # path('delete', studentdelete),
    # path('index', index),
    # path('indexx', indexx),

    # path('listt', stafflist),
    # path('insertt', staffinsert),
    # path('updatee', staffupdate),
    # path('deletee', staffdelete),

    # path('liststudent', liststudent),
    # path('liststaff', liststaff),
    # path('mainreports', mainreports),
    # path('login', login ,name='login'),
    # path('logout', logout ,name='logout'),
    # path('register/', register,name='register'),
    path('User/', include('users.urls')),
    path('staff/', include('staff.urls'))

]
