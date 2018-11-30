from django.db import models


class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    module_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, related_name='modules', on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)
    credit = models.IntegerField()
    time = models.IntegerField(default=0)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
