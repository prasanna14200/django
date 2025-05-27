from django.contrib import admin
from django.urls import path
from coder import views
app_name = 'coder'

urlpatterns = [
    path('', views.AddView.as_view(),name='index'),
    path('add/', views.Createmyview.as_view(),name='add'),
    path('delete/<int:pk>', views.Delete.as_view(),name='delete'),
    path('update/<int:pk>', views.EditView.as_view(),name='update'),



]