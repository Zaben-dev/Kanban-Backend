from rest_framework import serializers
from .models import Columns, Tasks

class ColumnsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Columns
        fields = ('id','name', 'limit')

        def __str__(self):
            return self.name

class TasksSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tasks
        fields = ('id','title','description','priority','difficulty','publishDate','column')

        def __str__(self):
            return self.title

