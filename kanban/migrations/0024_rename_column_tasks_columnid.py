# Generated by Django 3.2 on 2021-04-29 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0023_alter_tasks_column'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='column',
            new_name='columnId',
        ),
    ]