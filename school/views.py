from django.views import generic

from . import models as school_model
from . import serializers

from rest_framework import generics as rest_generic


class SubjectList(generic.ListView):
    template_name = 'school/subject_list.html'
    model = school_model.Subject
    context_object_name = 'subjects'


class ModuleAPI(rest_generic.ListAPIView):
    queryset = school_model.Module.objects.all()
    serializer_class = serializers.ModuleSerializer
