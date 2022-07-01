from django.urls import path,include
from staff.views import *

from staff.views import liststaff, insertstaff,insertuser

urlpatterns = [
    path('',liststaff),
    path('insert',insertstaff),
]