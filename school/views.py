from django.shortcuts import render
from django.views import generic

from . import models as school_model


class SubjectList(generic.ListView):
    template_name = 'school/subject_list.html'
    model = school_model.Subject
    context_object_name = 'subjects'
