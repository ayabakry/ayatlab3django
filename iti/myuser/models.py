from django.db import models

# Create your models here.
class myuser(models.Model):
    id=models.AutoField( primary_key=True)
    username=models.CharField(max_length=20)
    email=models.EmailField( max_length=20,null=True)
    password=models.CharField( max_length=8,null=True)
