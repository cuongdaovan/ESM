from rest_framework import serializers

from . import models


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Subject
        fields = ('__all__')


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = ('__all__')


class ModuleSerializer(serializers.ModelSerializer):
    # modules = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    faculty = serializers.StringRelatedField()

    class Meta:
        model = models.Module
        fields = ('__all__')
