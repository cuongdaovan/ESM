from django.db import models


class Term(models.Model):
    term_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField('starting date')
    end_date = models.DateField('end date')
