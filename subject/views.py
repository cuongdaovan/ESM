from django.views import generic

from . import models as subject_model


class SubjectList(generic.ListView):
    template_name = 'ESM.subject/subject_list.html'
    model = subject_model.Subject
    context_object_name = 'subjects'
