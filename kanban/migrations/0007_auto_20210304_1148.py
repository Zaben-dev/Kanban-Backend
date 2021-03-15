# Generated by Django 3.1.7 on 2021-03-04 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0006_auto_20210304_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')], default='Low', max_length=6)),
                ('difficulty', models.CharField(choices=[('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Hard', 'Hard')], default='Easy', max_length=12)),
                ('publishDate', models.DateTimeField(auto_now_add=True, verbose_name='date time published')),
            ],
            options={
                'ordering': ('priority',),
            },
        ),
        migrations.RenameModel(
            old_name='Column',
            new_name='Columns',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='tasks',
            name='column',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='column', to='kanban.columns'),
        ),
    ]