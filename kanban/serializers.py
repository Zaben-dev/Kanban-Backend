from rest_framework import serializers
from .models import Columns, Tasks
from django.core.exceptions import ValidationError

def validate_column_limit(value):
    c = Columns.objects.get(id=value)
    if c.limit is not None and Tasks.objects.filter(column_id=value).count() >= c.limit:
        raise ValidationError(
            "Can only create %s tasks in column '%s'." % (c.limit, c.name))

class ColumnsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Columns
        fields = ('id', 'name', 'limit')


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    column_id = serializers.IntegerField(required=False, validators=[validate_column_limit])
    columnId = column_id

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'priority', 'difficulty', 'publishDate', 'column', 'column_id',
                  'position','columnId' )

        def get_column_id(self, obj):
            obj.column_id = Columns.objects.get(id=self.model.column.id)
            col_id = obj.column_id.id
            return col_id
