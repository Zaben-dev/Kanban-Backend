# Generated by Django 3.1.5 on 2021-04-14 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0005_auto_20210414_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='rows',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='row',
                to='kanban.rows'),
        ),
    ]
