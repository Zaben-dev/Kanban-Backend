# Generated by Django 3.1.5 on 2021-04-29 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0019_auto_20210429_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='user',
            new_name='User',
        ),
    ]
