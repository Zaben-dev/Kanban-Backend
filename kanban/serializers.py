from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

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

    # column_id = serializers.IntegerField(required=False)
    # columnId = column_id
    columnId = serializers.PrimaryKeyRelatedField(many=False, queryset=Columns.objects.all())

    #row_id = serializers.IntegerField(required=False)
    rowId = serializers.PrimaryKeyRelatedField(many=False, queryset=Rows.objects.all())

    # User = get_user_model()
    # choices = User.objects.all()

    # user_id = serializers.IntegerField(choices = choices)
    # userId = user_id

    #ids = serializers.HyperlinkedRelatedField(many=True, queryset=User.objects.all(),view_name='User-list')
    #user = serializers.ReadOnlyField(source='User.username')
    User = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Tasks
        fields = ('id', 'User', 'title', 'description', 'priority', 'difficulty',
                  'publishDate', 'position','columnId','rowId')

        # def get_column_id(self, obj):
        #     obj.column_id = Columns.objects.get(id=self.model.column.id)
        #     col_id = obj.column_id.id
        #     return col_id

        # def get_row_id(self, obj):
        #     obj.row_id = Rows.objects.get(id=self.model.row.id)
        #     row_id = obj.row_id.id
        #     return row_id

        # def get_user_id(self, obj):
        #     obj.user_id = User.objects.get(id=self.model.User.id)
        #     user_id = obj.User_id.id
        #     return user_id


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


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class LoginSerializer(serializers.Serializer):
   username = serializers.CharField()
   password = serializers.CharField()

   def validate(self, data):
      user = authenticate(**data)
      if user and user.is_active:
         return user
      raise serializers.ValidationError("Incorrect Credentials")
