from django.db import models
from django.db import transaction


def checkPositions(col):
    print('-----col = %s-----'%col)

    countCols = Columns.objects.filter().count() #Number of columns
    colList = [] #array of columns

    if col > countCols-1:#If col is < than number of columns - End of function
        return 0

    for i in range(countCols): #Filling the columns array
        colList.append(Columns.objects.filter()[i:i+1].first()) 

    print('-----For column: %s-----'%colList[col])

    count = Tasks.objects.filter(column=colList[col]).count()#Number of tasks in current column
    tasList = [] #array of tasks

    for j in range(count): 
        tasList.append(Tasks.objects.filter(column=colList[col])[j:j+1].first()) #Filling the tasks array

    print('Number of tasks in column %s = %s'%(colList[col],count))
    
    min = Tasks.objects.filter(column=colList[col]).aggregate(smallest=models.Min('position'))['smallest'] #Find a minimum position in column

    print('Min position in column %s = %s'%(colList[col],min))

    if min is None: #If min is none - Column is empty - Change to the next column (col=col+1)
        print('Kolumna pusta - Zmieniono kolumne')
        checkPositions(col+1)

    if len(tasList) == 1: #If number of tasks on column is one - Change to the next column (col=col+1)
        print('One task in column - Column has been changed')
        checkPositions(col+1)
    
    if min != 1 and min is not None: #If min exists and min is not 1 - Change minimum to one
        with transaction.atomic():
            for task in Tasks.objects.filter(column=colList[col], position=min):
                min = 1
                task.position = min
                print('Minimum value wasn`t `1` - Minimum was changed to `1`')
                task.save(col=1)

    if min == 1: #If min is 1 - Column is not empty - Check positions
        for l in range (len(tasList)-1):
            if(tasList[l+1].position-tasList[l].position != 1):
                with transaction.atomic():
                    for task in Tasks.objects.filter(column=colList[col],position=tasList[l+1].position):
                        task.position = 1+tasList[l].position
                        task.save(col=1)
                        print('Changed position of task (id:%s) from |%s| to |%s|'%(tasList[l+1].id,tasList[l+1].position,1+tasList[l].position))
                        tasList[l+1].position = 1+tasList[l].position 
        print('Column has been changed')
        checkPositions(col+1)
        


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

    def save(self, col=-1, **kwargs):
        #col = 1 - Only save task
        #col = -1 - checkPositions(0)
        countCols = Columns.objects.filter().count()
        zmiana = True
        while zmiana:
            if Tasks.objects.filter(column=self.column,position=self.position).exists():
                with transaction.atomic():
                    for task in Tasks.objects.filter(column=self.column,position=self.position):
                        task.position = task.position+1
                        task.save(col=1)
                        zmiana=True
            else:
                zmiana= False
                super().save(**kwargs)

        if col == 1:
            super().save(**kwargs)

        if col == -1:
            checkPositions(0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['column_id','position']
