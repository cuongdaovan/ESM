from django.db import models

from ESM.school import models as school_model
from ESM.student import models as student_model


class Teacher(models.Model):
    teacher_code = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    teach_start_date = models.DateField('date start')
    education = models.TextField(max_length=1000)
    level = ('1', '2', '3')
    sex = ('female', 'male')
    date_of_birth = models.DateField('date of birth')
    faculty_code = models.ForeignKey(
        school_model.Faculty,
        on_delete=models.CASCADE,
        related_name='faculty_code'
    )
    password = models.CharField(max_length=50)


class TeacherSubject(models.Model):
    teacher_code = models.ForeignKey(Teacher, primary_key=True)
    subject_code = models.ForeignKey(school_model.Subject, primary_key=True)
    description = models.TextField(max_length=500)


class Evaluation(models.Model):
    evaluation_code = models.AutoField(primary_key=True)
    student = models.ForeignKey()
    teacher = models.ForeignKey(Teacher)
    time = models.TimeField()
    date = models.DateField()
    type = ('1', '2')
    content = models.TextField(max_length=1000)
