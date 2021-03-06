# Generated by Django 2.0 on 2021-04-15 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0009_auto_20210415_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cells',
            fields=[
                ('id',
                 models.AutoField(
                     primary_key=True,
                     serialize=False)),
                ('column',
                 models.ForeignKey(
                     editable=False,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='column',
                     to='kanban.Columns')),
                ('row',
                 models.ForeignKey(
                     editable=False,
                     null=True,
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='row',
                     to='kanban.Rows')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={
                'ordering': ['position']},
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='column',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='row',
        ),
        migrations.AddField(
            model_name='tasks',
            name='cell',
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name='cell',
                to='kanban.Cells'),
        ),
    ]
