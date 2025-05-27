
from django.contrib import admin
from django.urls import path
from coder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coder_details/',views.details),
]
