from rest_framework import serializers
from .models import Columns, Tasks
import attr

class ColumnsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Columns
        fields = ('id','name', 'limit')

        def __str__(self):
            return self.id

class TasksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tasks
        #tasks_serializer_class = TasksListSerializer
        fields = ('id','title','description','priority','difficulty','publishDate','column')

        def __str__(self):
            return self.title