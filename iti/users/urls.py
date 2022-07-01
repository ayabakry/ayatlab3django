from django.urls import path , include

from staff.views import insertuser

# from .views import classbaseddelete, listuser, Update,Delete
from users.views import classbaseddelete,listuser,Update,Delete,uppdateviews

urlpatterns = [
path('',listuser),
# path('insertt', insertuser),
path('update/<id>',Update,name='updateuser'),
path('delete/<id>',Delete,name='deleteuser'),
path('classbaseddelete',classbaseddelete.as_view()),
path('uppdateviews/',uppdateviews.as_view())
]