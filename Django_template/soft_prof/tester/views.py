from django.shortcuts import render

# Create your views here.

def jrtester(request):
         return render(request,'tester/jrtester.html')

def srtester(request):
         return render(request,'tester/srtester.html')


