from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from django.db import transaction


class ColumnsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Columns
        fields = ('id', 'name', 'limit')


class TasksSerializer(serializers.HyperlinkedModelSerializer):

    column_id = serializers.IntegerField(required=False)
    columnId = column_id

    row_id = serializers.IntegerField(required=False)
    rowId = row_id

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'priority', 'difficulty',
                  'publishDate', 'position','column', 'column_id', 'columnId','row','row_id','rowId')

        def get_column_id(self, obj):
            obj.column_id = Columns.objects.get(id=self.model.column.id)
            col_id = obj.column_id.id
            return col_id

        def get_row_id(self, obj):
            obj.row_id = Rows.objects.get(id=self.model.row.id)
            row_id = obj.row_id.id
            return row_id


class RowsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rows
        fields = ('id', 'name')

