from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
         path('',views.index,name='index'),
         path('about/',views.about,name='about'),
         path('skill/',views.skill,name='skill'),
         path('work/',views.work,name='work'),
         path('contact/',views.contact,name='contact'),
   
]