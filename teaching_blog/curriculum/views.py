
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, FormView,CreateView,UpdateView,DeleteView)
from .models import *
from . import forms
from django.urls import reverse_lazy




# Create your views here.
class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class SubjectListView(DetailView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/subject_list_view.html'
    
class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'

class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model= Lesson
    template_name = 'curriculum/lesson_detail_view.html'
    
class LessonCreateView(CreateView):
    form_class = forms.LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('curriculum:lesson_list',kwargs={'standard':standard.slug,'slug':self.object.slug})

    def form_valid(self,form,*args, **kwargs):
        self.object = self.get_object()
        #data shouldn't be saved yet
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())



# class LessonUpdateView(UpdateView):
#     fields = ('name','position','video','ppt','Notes')