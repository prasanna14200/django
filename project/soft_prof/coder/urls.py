


from django.contrib import admin
from django.urls import path
from coder import views 

urlpatterns = [
    
    path('jrcoder',views.jrcoder),
    path('srcoder',views.srcoder),
 

]
