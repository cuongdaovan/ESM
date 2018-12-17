from django.db import models
from django.contrib.auth import models
from django.db import models as db_models


class User(models.User):
    __type__ = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    type = db_models.CharField(
        max_length=50,
        default='',
        choices=__type__
    )
