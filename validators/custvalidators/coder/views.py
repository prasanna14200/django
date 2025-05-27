from django.shortcuts import render
from . forms import coderform
# Create your views here.

def coderdetails(request):
         if request.method=="POST":
                 fm=coderform(request.POST)
                 if fm.is_valid():
                         nm=fm.cleaned_data['name']
                         des=fm.cleaned_data['designation']
                         dept=fm.cleaned_data['department']
                         em=fm.cleaned_data['email']
         else:
                 fm=coderform()
         return render(request,'coder/index.html',{'form':fm})                
                 


