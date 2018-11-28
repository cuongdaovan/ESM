from django.shortcuts import render
from django.views import generic
from student import models as student_model

class AssessmentUpdate(generic.edit.CreateView):
    model = student_model.SjAssessment
    fields = [
        'student',
        'subject',
        'content',
        'time',
        'date',
    ]
    template_name = 'sj_assessment/base.html'
