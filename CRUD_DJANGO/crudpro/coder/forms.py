from django import forms
from .models import CoderModel

class coderForm(forms.ModelForm):
         class Meta:
                 model=CoderModel
                 fields="__all__"
                 widgets={'name':forms.TextInput(attrs={'class':'form-control'})
                          ,'designation':forms.TextInput(attrs={'class':'form-control'}),
                          'email':forms.EmailInput(attrs={'class':'form-control'}),
                          'yoe':forms.TextInput(attrs={'class':'form-control'})}