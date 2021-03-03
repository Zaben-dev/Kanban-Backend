from django.db import models

class Column(models.Model):
    name = models.CharField(max_length=200)
    limit = models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Easy = "Easy"
    Intermediate = "Intermediate"
    Hard = "Hard"
    title = models.CharField(max_length=100)
    description = models.TextField()
    selectPriority = ((Low, 'Low'), (Medium, 'Medium'), (High, 'High'),)
    selectDifficulty = ((Easy, 'Easy'), (Intermediate, 'Intermediate'), (Hard, 'Hard'),)
    priority = models.CharField(max_length=6,choices=selectPriority,default=Low)
    difficulty = models.CharField(max_length=12,choices=selectDifficulty,default=Easy)
    publishDate = models.DateTimeField('date time published', auto_now_add=True)
    column = models.ForeignKey(Column, related_name="column", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('priority',)
        
# Create your models here.
