from django.contrib import admin
from django.urls import path,include
from tester import views

urlpatterns = [
    
    path('jrtester/',views.jrtester),
    path('srtester/',views.srtester),

]
