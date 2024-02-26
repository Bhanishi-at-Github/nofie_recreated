# Generated by Django 5.0.2 on 2024-02-26 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nofie_app', '0003_teacher_department_alter_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='nofie_app.teacher'),
        ),
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(default='Untitled', max_length=100),
        ),
    ]