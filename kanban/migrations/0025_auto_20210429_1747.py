# Generated by Django 3.2 on 2021-04-29 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0024_rename_column_tasks_columnid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['position']},
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='row',
        ),
        migrations.AddField(
            model_name='tasks',
            name='rowId',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rowId', to='kanban.rows'),
        ),
    ]