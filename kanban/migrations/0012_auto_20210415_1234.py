# Generated by Django 2.0 on 2021-04-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0011_auto_20210415_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cells',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]