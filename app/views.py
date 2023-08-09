from django.shortcuts import render

# Create your views here.

from app.models import*
from django.views.generic import ListView,DetailView,CreateView,UpdateView

class SchoolList(ListView):
    model=School
    context_object_name='allSO'




class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'



class SchoolCreate(CreateView):
    model=School
    fields="__all__"


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
    
    
