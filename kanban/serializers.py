from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.models import User

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

    # cell_id = serializers.IntegerField(required=False)
    # cellId = cell_id

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

        # def get_cell_id(self, obj):
        #     obj.cell_id = Cells.objects.get(id=self.model.cell.id)
        #     cell_id = obj.cell_id.id
        #     return cell_id


class RowsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rows
        fields = ('id', 'name')

# class CellsSerializer(serializers.HyperlinkedModelSerializer):

#     column_id = serializers.IntegerField(required=False)
#     columnId = column_id

#     row_id = serializers.IntegerField(required=False)
#     rowId = row_id

#     class Meta:
#         model = Cells
#         fields = ('column','row','id','column_id','columnId', 'row_id','rowId')

#         def get_column_id(self, obj):
#             obj.column_id = Columns.objects.get(id=self.model.column.id)
#             col_id = obj.column_id.id
#             return col_id

#         def get_row_id(self, obj):
#             obj.row_id = Rows.objects.get(id=self.model.row.id)
#             row_id = obj.row_id.id
#             return row_id

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user