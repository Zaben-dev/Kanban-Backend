from django.db import models
from django.db import transaction

def checkPositions(col):
    countCols = Columns.objects.filter().count()
    colList = []
    for i in range(countCols):
        colList.append(Columns.objects.filter()[i:i+1].first())
    min = Tasks.objects.filter(column=colList[col]).aggregate(smallest=models.Min('position'))['smallest']
    if min != 1:
        with transaction.atomic():
            for task in Tasks.objects.filter(column=colList[col], position=min):
                min = 1
                task.position = min
                task.save(col=999)
    count = Tasks.objects.filter(column=colList[col]).count()
    tab = []
    if min == 1:
        for k in range(count):
            tab.append(Tasks.objects.filter(column=colList[col])[k:k+1].first())
        for l in range (len(tab)-1):
            if(tab[l+1].position-tab[l].position != 1):
                with transaction.atomic():
                    for task in Tasks.objects.filter(column=colList[col],position=tab[l+1].position):
                        task.position = 1+tab[l].position
                        tab[l+1].position = 1+tab[l].position
                        task.save(col=999)
                        if l == (len(tab)-2):
                            task.save(col=col+1)

class Columns(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    limit = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

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
    publishDate = models.DateTimeField('date time published', auto_now_add=True)
    column = models.ForeignKey(Columns, related_name="column", on_delete=models.PROTECT, editable=False)
    position = models.IntegerField('Code', default=1, unique=False, editable=True)

    def delete(self):
        super(Tasks, self).delete()
        checkPositions(0)

    def save(self, col=1000, **kwargs):
        countCols = Columns.objects.filter().count()
        zmiana = True
        while zmiana:
            if Tasks.objects.filter(column=self.column,position=self.position).exists():
                with transaction.atomic():
                    for task in Tasks.objects.filter(column=self.column,position=self.position):
                        task.position = task.position+1
                        task.save(col=999)
                        zmiana=True
            else:
                zmiana= False
                super().save(**kwargs)
        if col == 999:
            super().save(**kwargs)

        if col == 1000:
            checkPositions(0)

        if col <= countCols:
            checkPositions(col)               

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['column_id','position']
