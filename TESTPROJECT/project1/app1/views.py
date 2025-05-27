from django.shortcuts import render
from .forms import app_reg
# Create your views here.

def display_form(request):
         if request.method=="POST":
                 fm=app_reg(request.POST)
                 if fm.is_valid():
                         print("Data is validated")
                         print(fm.cleaned_data['name'])
                         print(fm.cleaned_data['email'])
         else:
             fm=app_reg()
         return render(request,'app1/index.html',{'form':fm})