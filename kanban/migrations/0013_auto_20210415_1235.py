# Generated by Django 2.0 on 2021-04-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0012_auto_20210415_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cells',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]