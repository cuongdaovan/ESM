from django.contrib import admin
from django import forms

from . import models as student_model


# class StudentForm(forms.ModelForm):
#     class Meta:
#         password = forms.CharField(max_length=32, widget=forms.PasswordInput)
#         model = student_model.Student
#         fields = ('password',)


# class StudentAdmin(admin.ModelAdmin):
#     exclude = ['password']
#     form = StudentForm


admin.site.register(student_model.Student)
admin.site.register(student_model.SjAssessment)
