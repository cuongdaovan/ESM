from django.db import models

from school import models as school_model
from student import models as student_model


class SubjectReview(models.Model):
    subject = models.ForeignKey(school_model.Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(student_model.Student, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    time = models.TimeField()
    date = models.DateField()
