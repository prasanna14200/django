from django.shortcuts import render

# Create your views here.

def index(request):
         return render(request,'myapp/index.html')


def about(request):
        return render(request,'myapp/about.html')

def skill(request):
        return render(request,'myapp/skill.html')

def work(request):
        return render(request,'myapp/work.html')

def contact(request):
        return render(request,'myapp/contact.html')