# Generated by Django 3.1.5 on 2021-04-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_auto_20210331_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rows',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
