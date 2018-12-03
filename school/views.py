from django.views import generic
from django.shortcuts import get_object_or_404

from . import models as school_model
from . import serializers

from rest_framework import generics as rest_generic
from rest_framework import viewsets
from rest_framework.response import Response


class SubjectList(generic.ListView):
    template_name = 'school/subject_list.html'
    model = school_model.Subject
    context_object_name = 'subjects'


class ModuleApi(viewsets.ViewSet):

    def list(self, request):
        queryset = school_model.Module.objects.all()
        serializer = serializers.ModuleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = school_model.Module.objects.all()
        module = get_object_or_404(queryset, pk=pk)
        serializer = serializers.ModuleSerializer(module)
        return Response(serializer.data)


class SubjectApi(viewsets.ViewSet):

    def list(self, request):
        queryset = school_model.Subject.objects.all()
        serializer = serializers.SubjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = school_model.Subject.objects.all()
        subject = get_object_or_404(queryset, pk=pk)
        serializer = serializers.SubjectSerializer(subject)
        return Response(serializer.data)
