# Generated by Django 3.2 on 2021-05-06 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0027_tasks_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='User',
        ),
    ]