from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from django.db import transaction



class ColumnsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Columns
        fields = ('id', 'name', 'limit')


class TasksSerializer(serializers.HyperlinkedModelSerializer):

    def validate_column_limit(value):
        if value is not None:
            c = Columns.objects.get(id=value)
            if c.limit is not None and Tasks.objects.filter(column_id=value).count() >= c.limit:
                raise ValidationError(
                    "Can only create %s tasks in column '%s'." % (c.limit, c.name))

    column_id = serializers.IntegerField(required=False, validators=[validate_column_limit])
    columnId = column_id

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'priority', 'difficulty', 'publishDate', 'column', 'column_id',
                  'position','columnId', 'rows')

        def get_column_id(self, obj):
            obj.column_id = Columns.objects.get(id=self.model.column.id)
            col_id = obj.column_id.id
            return col_id


class RowsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rows
        fields = ('id', 'name')
