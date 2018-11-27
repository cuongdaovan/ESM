# Generated by Django 2.1.2 on 2018-11-27 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='level',
            field=models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='teacher',
            name='sex',
            field=models.CharField(blank=True, choices=[('female', 'female'), ('male', 'female')], default='', max_length=10),
        ),
    ]