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
        fields = ('id', 'title', 'description', 'priority', 'difficulty', 'publish_date', 'column', 'column_id','position')

        def get_column_id(self, obj):
            obj.column_id = Columns.objects.get(id=self.model.column.id)
            col_id = obj.column_id.id
            return col_id
