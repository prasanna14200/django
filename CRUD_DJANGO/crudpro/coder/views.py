from django.shortcuts import render
from .models import CoderModel
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

#def CoderModel(request):
 #        return render(request,'coder/index.html')

class AddView(ListView):
     model=CoderModel
     template_name='coder/index.html'
     context_object_name='index-object'

class Createmyview(CreateView):
     model=CoderModel
     template_name='coder/add.html'
     fields='__all__'
     success_url=reverse_lazy('coder:index')

class Delete(DeleteView):
     model=CoderModel
     pk_url_kwarg='pk'
     success_url=reverse_lazy('coder:index')
     template_name='coder/confirm_delete.html'

class EditView(UpdateView):
     model=CoderModel
     template_name='coder/edit.html'
     fields='__all__'
     pk_url_kwarg='pk'
     success_url=reverse_lazy('coder:index')


