# Generated by Django 3.1.5 on 2021-04-29 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0014_auto_20210426_1906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['row', 'position']},
        ),
    ]