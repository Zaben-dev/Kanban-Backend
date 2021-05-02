from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def checkColumnLimit(col, row, id):
    if col is not None:
        c = Columns.objects.get(id=col)
        if Tasks.objects.filter(
                id=id,
                columnId=col,
                rowId=row).exists() == False:
            if c.limit is not None and Tasks.objects.filter(
                    columnId=col, rowId=row).count() >= c.limit:
                raise ValidationError(
                    "Can only create %s tasks in column '%s'." %
                    (c.limit, c.name))

def checkPositions(col):
    print('-----col = %s-----'%col)

    countCols = Columns.objects.filter().count() #Number of columns
    countRows = Rows.objects.filter().count() #Number of rows
    colList = [] #array of columns
    rowList = [] #array of rows

    if col > countCols-1:#If col is < than number of columns - End of function
        return 0

    for i in range(countCols): #Filling the columns array
        colList.append(Columns.objects.filter()[i:i+1].first()) 

    for i in range(countRows): #Filling the rows array
        rowList.append(Rows.objects.filter()[i:i+1].first()) 

    print('-----For column: %s-----'%colList[col])

    for i in range(countRows):
        print('i=%s'%(i))
        count = Tasks.objects.filter(columnId=colList[col],rowId=rowList[i]).count()#Number of tasks in current column and row
        tasList = [] #array of tasks


        for j in range(count): 
            tasList.append(Tasks.objects.filter(columnId=colList[col],rowId=rowList[i])[j:j+1].first()) #Filling the tasks array

        print('Number of tasks in col %s and row %s = %s'%(colList[col],rowList[i],count))
    
        min = Tasks.objects.filter(columnId=colList[col],rowId=rowList[i]).aggregate(smallest=models.Min('position'))['smallest'] #Find a minimum position in column

        print('Min position in col %s and row %s = %s'%(colList[col],rowList[i],min))

        if min is None: #If min is none - Column is empty - Change to the next column (col=col+1)
            print('Komórka pusta - Zmieniono komórke')
            continue
   
        if min != 1 and min is not None: #If min exists and min is not 1 - Change minimum to one
            with transaction.atomic():
                for task in Tasks.objects.filter(columnId=colList[col],rowId=rowList[i], position=min):
                    min = 1
                    task.position = min
                    print('Minimum value wasn`t `1` - Minimum was changed to `1`')
                    tasList[0]=task
                    task.save(col=1)

        if len(tasList) == 2:
            tasList.sort(key=lambda x: x.position)

        else:
            if tasList[len(tasList)-1].position>count:
                temp = tasList[len(tasList)-2]
                tasList[len(tasList)-2]= tasList[len(tasList)-1]
                tasList[len(tasList)-1]=temp

            if len(tasList) == 1: #If number of tasks on column is one - Change to the next column (col=col+1)
                print('One task in col - column has been changed')
                continue
    
        #If min is 1 - Column is not empty - Check positions
        for l in range (len(tasList)-1):
            if(tasList[l+1].position-tasList[l].position != 1):
                with transaction.atomic():
                    for task in Tasks.objects.filter(columnId=colList[col],rowId=rowList[i],position=tasList[l+1].position):
                        task.position = 1+tasList[l].position
                        task.save(col=1)
                        print('Changed position of task (id:%s) from |%s| to |%s|'%(tasList[l+1].id,tasList[l+1].position,1+tasList[l].position))
                        tasList[l+1].position = 1+tasList[l].position 
    print('Column has been changed')
    checkPositions(col+1)


class Columns(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    limit = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Rows(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

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
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=400, blank=True)
    selectPriority = ((Low, 'Low'), (Medium, 'Medium'), (High, 'High'),)
    selectDifficulty = ((Easy, 'Easy'), (Intermediate,
                        'Intermediate'), (Hard, 'Hard'),)
    priority = models.CharField(
        max_length=6,
        choices=selectPriority,
        default=Low)
    difficulty = models.CharField(
        max_length=12,
        choices=selectDifficulty,
        default=Easy)
    publishDate = models.DateTimeField(
        'date time published', auto_now_add=True)
    columnId = models.ForeignKey(
        Columns,
        related_name="columnId",
        null=True,
        on_delete=models.PROTECT,
        editable=False)
    position = models.IntegerField(
        'Position',
        default=1,
        unique=False,
        editable=True)
    rowId = models.ForeignKey(
        Rows,
        related_name="rowId",
        null=True,
        on_delete=models.PROTECT,
        editable=False)

    # User = models.ManyToManyField(
    #     'auth.User',
    #     related_name='danie',
    #     editable=True)

    def delete(self):
        super(Tasks, self).delete()
        checkPositions(0)

    def save(self, col=-1, **kwargs):
        checkColumnLimit(self.columnId.id, self.rowId.id, self.id)
        # col = 1 - Only save task
        #col = -1 - checkPositions(0)

        zmiana = True
        while zmiana:
            if Tasks.objects.filter(columnId=self.columnId,rowId=self.rowId,position=self.position).exists():
                with transaction.atomic():
                    for task in Tasks.objects.filter(columnId=self.columnId,rowId=self.rowId,position=self.position):
                        task.position = task.position + 1
                        task.save(col=1)
                        zmiana = True
            else:
                zmiana = False
                super().save(**kwargs)

        if col == 1:
            super().save(**kwargs)

        if col == -1:
            checkPositions(0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['columnId','rowId','position']
