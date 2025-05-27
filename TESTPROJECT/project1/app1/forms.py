from django import forms

class app_reg(forms.Form):
         name=forms.CharField()
         email=forms.EmailField()

         def clean(self):
                 cleaned_data=super().clean()
                 namedata=self.cleaned_data['name']
                 emaildata=self.cleaned_data['email']
                 if len(namedata)<3:
                         raise forms.ValidationError('The name should contain 3 characters')
                 if len(emaildata)<8:
                         raise forms.ValidationError('The email should contaIN MORE THAN 8 CHARACTERS') 
                 