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
    l = (
        (1, 'level 1'),
        (2, 'level 2'),
        (3, 'level 3'),
    )
    level = models.IntegerField(choices=l, default=1, blank=True)
    s = (
        ('female', 'female'),
        ('male', 'male'),
    )
    sex = models.CharField(max_length=10, choices=s, default='', blank=True)
    date_of_birth = models.DateField()
    faculty_code = models.ForeignKey(
        school_model.Faculty,
        on_delete=models.CASCADE,
        related_name='faculties'
    )
    email = models.EmailField(default='', blank=True)
    password = models.CharField(max_length=50)


# class Evaluation(models.Model):
#     evaluation_code = models.AutoField(primary_key=True)
#     student = models.ForeignKey(student_model)
#     teacher = models.ForeignKey(Teacher)
#     time = models.TimeField()
#     date = models.DateField()
#     type = ('1', '2')
#     content = models.TextField(max_length=1000)
