
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, FormView)
from .models import *


# Create your views here.
class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subject_list_view.html'
    