from django import forms
from .models import *
from myuser.models import myuser


class InsertTrainee(forms.Form):
    name = forms.CharField(max_length=50)
    nationalnum = forms.IntegerField()
    trainer = forms.ChoiceField(choices=[(1,'alyaa'),(2,'asmaa')])

class InsertUser(forms.ModelForm):
    class Meta:
        model=myuser
        fields='__all__'


