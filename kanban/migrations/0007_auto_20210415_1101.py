# Generated by Django 2.0 on 2021-04-15 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0006_auto_20210414_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='rows',
        ),
        migrations.AddField(
            model_name='tasks',
            name='row',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='row',
                to='kanban.Rows'),
        ),
    ]
