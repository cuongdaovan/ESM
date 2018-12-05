from django.db import models

from school import models as school_model


class Student(models.Model):
    student_id = models.BigIntegerField(
        primary_key=True,
        default=0
    )
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    hometown = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    __status__ = (
        ('TH', 'bi thoi hoc'),
        ('RT', 'ra truong'),
    )
    status = models.CharField(
        choices=__status__,
        max_length=10,
        default=''
    )
    # mark = models.ForeignKey()
    # class_s = models.ForeignKey()
    __sex__ = (
        ('female', 'female'),
        ('male', 'male')
    )
    sex = models.CharField(
        max_length=10,
        choices=__sex__,
        default=''
    )
    email = models.EmailField()
    password = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    faculty = models.ForeignKey(
        school_model.Faculty,
        on_delete=models.CASCADE,
        related_name='students'
    )
    subject_assessments = models.ManyToManyField(
        school_model.Subject,
        through='SjAssessment',
    )

    def __str__(self):
        return self.full_name


class SjAssessment(models.Model):
    subject = models.ForeignKey(
        school_model.Subject,
        on_delete=models.CASCADE,
        related_name='assessments'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='st_assessments',
    )
    content = models.TextField(max_length=1000)
    time = models.TimeField()
    date = models.DateField()

