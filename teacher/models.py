from django.db import models

from school import models as school_model


class Teacher(models.Model):
    teacher_code = models.AutoField(primary_key=True)
    subject = models.ManyToManyField(school_model.Subject)
    full_name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    teach_start_date = models.DateField()
    education = models.TextField(max_length=1000)
    level = ('1', '2', '3')
    sex = ('female', 'male')
    date_of_birth = models.DateField()
    faculty_code = models.ForeignKey(
        school_model.Faculty,
        on_delete=models.CASCADE,
        related_name='faculties'
    )
    password = models.CharField(max_length=50)

# class Evaluation(models.Model):
#     evaluation_code = models.AutoField(primary_key=True)
#     student = models.ForeignKey(student_model)
#     teacher = models.ForeignKey(Teacher)
#     time = models.TimeField()
#     date = models.DateField()
#     type = ('1', '2')
#     content = models.TextField(max_length=1000)
