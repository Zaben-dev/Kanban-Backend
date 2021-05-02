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
            if c.limit is not None and Tasks.objects.filter(
                    column_id=value).count() >= c.limit:
                raise ValidationError(
                    "Can only create %s tasks in column '%s'." %
                    (c.limit, c.name))

    columnId = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Columns.objects.all())
    rowId = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Rows.objects.all())
    #User = serializers.PrimaryKeyRelatedField(
    #    many=True, queryset=User.objects.all())

    class Meta:
        model = Tasks
        fields = (
            'id',
            #'User',
            'title',
            'description',
            'priority',
            'difficulty',
            'publishDate',
            'position',
            'columnId',
            'rowId')


class RowsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rows
        fields = ('id', 'name')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
