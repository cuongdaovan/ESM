from django.contrib import admin

from . import models as teacher_model

admin.site.register(teacher_model.Teacher)