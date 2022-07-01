# from django.db import models
#
# class Trainer(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     courses=models.CharField(max_length=200)
#
# # Create your models here.
# class Trainee (models.Model):
#     id= models.AutoField(primary_key=True)
#     name= models.CharField(max_length=200)
#     nationalnum= models.IntegerField()
#     trainer= models.ForeignKey(Trainer,on_delete=models.CASCADE)