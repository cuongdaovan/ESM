from rest_framework import serializers

from student import models as student_model


class AssessmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()

    class Meta:
        model = student_model.SjAssessment
        fields = (
            'id',
            'subject',
            'student',
            'content',
            'date',
            'time'
        )
