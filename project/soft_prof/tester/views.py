from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def jrtester(request):
         return render(request,'jrtester.html')
def srtester(request):
        return render(request,'srtester.html')
