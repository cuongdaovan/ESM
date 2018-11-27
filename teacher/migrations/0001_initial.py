# Generated by Django 2.1.2 on 2018-11-26 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0003_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_code', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('hometown', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
                ('teach_start_date', models.DateField()),
                ('education', models.TextField(max_length=1000)),
                ('date_of_birth', models.DateField()),
                ('password', models.CharField(max_length=50)),
                ('faculty_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculties', to='school.Faculty')),
                ('subject', models.ManyToManyField(to='school.Subject')),
            ],
        ),
    ]
