# Generated by Django 2.1.2 on 2018-11-26 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='major',
            old_name='major_code',
            new_name='major_id',
        ),
    ]
