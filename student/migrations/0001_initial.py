# Generated by Django 2.1.2 on 2018-11-27 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0006_delete_major'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('hometown', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('TH', 'bi thoi hoc'), ('RT', 'ra truong')], default='', max_length=10)),
                ('sex', models.CharField(choices=[('female', 'female'), ('male', 'male')], default='', max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=100)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='school.Faculty')),
            ],
        ),
    ]
