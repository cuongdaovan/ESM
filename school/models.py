from django.db import models


class Faculty(models.Model):
    faculty_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)


class Major(models.Model):
    major_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type_of_training = ('type')
    history = models.TextField(max_length=1000)


class Term(models.Model):
    term_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField('starting date')
    end_date = models.DateField('end date')


class Subject(models.Model):
    subject_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
