# Generated by Django 2.0 on 2021-03-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='publishDate',
            field=models.DateTimeField(verbose_name='date time published'),
        ),
    ]
