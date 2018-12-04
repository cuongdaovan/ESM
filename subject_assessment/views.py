from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from student import models as student_model
from . import serializers

from rest_framework import viewsets
from rest_framework.response import Response


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


class AssessmentApi(viewsets.ModelViewSet):

    queryset = student_model.SjAssessment.objects.all()
    serializer_class = serializers.AssessmentSerializer

    # def create(self, request):
    #     queryset = student_model.SjAssessment.objects.all()
    #     serializer = serializers.AssessmentSerializer(queryset, many=True)
    #     return Response(serializer.data)
