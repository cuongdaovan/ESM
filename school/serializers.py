from rest_framework import serializers

from . import models
from subject_assessment import serializers as sa_serializer
from student import serializers as st_serializer


class SubjectSerializer(serializers.ModelSerializer):
    assessments = sa_serializer.AssessmentSerializer(many=True)

    class Meta:
        model = models.Subject
        fields = (
            'subject_id',
            'name',
            'description',
            'assessments',
        )


class ModuleSerializer(serializers.ModelSerializer):
    # modules = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()
    faculty = serializers.StringRelatedField()

    class Meta:
        model = models.Module
        fields = (
            'module_id',
            'subject',
            'subject_id',
            'faculty',
            'name',
            'description',
            'credit',
            'time'
        )


class FacultySerializer(serializers.ModelSerializer):
    faculty_modules = ModuleSerializer(many=True)
    # students = st_serializer.StudentSerializer(many=True)

    class Meta:
        model = models.Faculty
        fields = (
            'faculty_id',
            'name',
            'description',
            'faculty_modules',
            'students',
        )
