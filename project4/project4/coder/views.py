from django.shortcuts import render
from coder.models import *


# Create your views here.\

def details(request):
         coder_info=coder_model.objects.all()
         return render(request,'coder/index.html',{'record':coder_info})


