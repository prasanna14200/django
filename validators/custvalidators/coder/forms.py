from django import forms
from django.core import validators


def name_start_with_G(value):
        if value[0]!='G':
                raise forms.ValidationError('Name start with G only')
        

class coderform(forms.Form):
         name=forms.CharField(validators=[name_start_with_G])
         designation=forms.CharField()
         department=forms.CharField()
         email=forms.EmailField()
