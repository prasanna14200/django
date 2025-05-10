from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def jrcoder(request):
         return render(request,'jrcoder.html')
def srcoder(request):
        return render(request,'srcoder')