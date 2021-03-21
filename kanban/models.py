from django.db import models
from django.core.exceptions import ValidationError
from django.db import transaction

def validate_column_limit(value):
    model = value
    c = Columns.objects.get(id=model.id)
    if c.limit is not None and Tasks.objects.filter(column=value).count() >= c.limit:
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
    priority = models.CharField(max_length=6, choices=selectPriority, default=Low)
    difficulty = models.CharField(max_length=12, choices=selectDifficulty, default=Easy)
    publish_date = models.DateTimeField('date time published', auto_now_add=True)
    column = models.ForeignKey(Columns, related_name="column", on_delete=models.PROTECT,
                               validators=[validate_column_limit],editable=False)
    position = models.IntegerField(('Code'),default=1,unique=False,editable=True)

    def delete(self):
        super(Tasks, self).delete()
        min = Tasks.objects.filter(column=self.column).aggregate(smallest=models.Min('position'))['smallest']
        if min != 1:
            with transaction.atomic():
                for task in Tasks.objects.filter(column=self.column,position=min):
                    min = 1
                    task.position = min
                    task.save()
        count = Tasks.objects.filter(column=self.column).count()
        tab = []
        if min == 1:
            for i in range(count):
                tab.append(Tasks.objects.filter(column=self.column)[i:i+1].first())
            for j in range (len(tab)-1):
                if(tab[j+1].position-tab[j].position != 1):
                    with transaction.atomic():
                        for task in Tasks.objects.filter(column=self.column,position=tab[j+1].position):
                            task.position = 1+tab[j].position
                            task.save()
                            tab[j+1].position = 1+tab[j].position

    def save(self, *args, **kwargs):
        zmiana = True
        while zmiana:
            if Tasks.objects.filter(column=self.column,position=self.position).exists():
                with transaction.atomic():
                    for task in Tasks.objects.filter(column=self.column,position=self.position):
                        task.position = task.position+1
                        task.save()
                        zmiana=True
            else:
                zmiana= False
        super(Tasks,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('column_id','position',)
