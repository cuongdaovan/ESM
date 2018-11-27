from django.db import models

from school import models as school_model


# student table
class Student(models.Model):
    student_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    hometown = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    _status = (
        ('TH', 'bi thoi hoc'),
        ('RT', 'ra truong'),
    )
    status = models.CharField(choices=_status, max_length=10, default='')
    # mark = models.ForeignKey()
    # class_s = models.ForeignKey()
    _sex = (
        ('female', 'female'),
        ('male', 'male')
    )
    sex = models.CharField(max_length=10, choices=_sex, default='')
    email = models.EmailField()
    password = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    faculty = models.ForeignKey(
        school_model.Faculty,
        on_delete=models.CASCADE,
        related_name='students'
    )
