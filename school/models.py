from django.db import models


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    type_of_training = ('')
    history = models.TextField(max_length=1000, blank=True)


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, related_name='modules', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    credit = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.name
