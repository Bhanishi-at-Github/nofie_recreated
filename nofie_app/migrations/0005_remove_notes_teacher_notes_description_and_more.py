# Generated by Django 5.0.2 on 2024-02-26 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nofie_app', '0004_notes_teacher_notes_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='teacher',
        ),
        migrations.AddField(
            model_name='notes',
            name='description',
            field=models.TextField(default='No Description'),
        ),
        migrations.AddField(
            model_name='notes',
            name='semester',
            field=models.IntegerField(default=1),
        ),
    ]
