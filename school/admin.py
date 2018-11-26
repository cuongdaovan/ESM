from django.contrib import admin

from . import models as school_model

admin.site.register(school_model.Subject)
admin.site.register(school_model.Faculty)
admin.site.register(school_model.Module)

