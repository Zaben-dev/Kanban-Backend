from rest_framework import serializers
from .models import Columns, Tasks


class ColumnsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Columns
        fields = ('id', 'name', 'limit')


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    column_id = serializers.IntegerField(required=False)

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'priority', 'difficulty', 'publishDate', 'column', 'column_id')

        def get_column_id(self, obj):
            obj.column_id = Columns.objects.get(id=self.model.column.id)
            id = obj.column_id.id
            return id
