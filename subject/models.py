from django.db import models


class Subject(models.Model):
    subject_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=False)