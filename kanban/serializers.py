from rest_framework import serializers
from .models import Column, Task

class ColumnSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Column
        fields = ('name', 'limit')

        def __str__(self):
            return self.name

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('title','description','priority','difficulty','publishDate','column')

        def __str__(self):
            return self.title

