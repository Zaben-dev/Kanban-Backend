from django.db import models
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseForbidden

#Validation of number of tasks in column:
def validate_column_limit(value):
    model = value
    c = Columns.objects.get(id=model.id)
    if ((c.limit is not None) and (Tasks.objects.filter(column=value).count() > c.limit)):
        raise ValidationError(
            "Can only create %s tasks in column '%s'." % (c.limit, c.name))

class Columns(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    limit = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Easy = "Easy"
    Intermediate = "Intermediate"
    Hard = "Hard"
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    selectPriority = ((Low, 'Low'), (Medium, 'Medium'), (High, 'High'),)
    selectDifficulty = ((Easy, 'Easy'), (Intermediate, 'Intermediate'), (Hard, 'Hard'),)
    priority = models.CharField(max_length=6,choices=selectPriority,default=Low)
    difficulty = models.CharField(max_length=12,choices=selectDifficulty,default=Easy)
    publishDate = models.DateTimeField('date time published', auto_now_add=True)
    column = models.ForeignKey(Columns, related_name="column", on_delete=models.PROTECT, validators=[validate_column_limit],)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('priority',)

           
# Create your models here.
