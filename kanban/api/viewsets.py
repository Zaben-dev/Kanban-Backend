from ..serializers import *
from rest_framework import viewsets
from django_filters import rest_framework as filters


class TasksFilter(filters.FilterSet):
    id = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description')


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filterset_class = TasksFilter


class ColumnsViewSet(viewsets.ModelViewSet):
    queryset = Columns.objects.all()
    serializer_class = ColumnsSerializer


class RowsViewSet(viewsets.ModelViewSet):
    queryset = Rows.objects.all()
    serializer_class = RowsSerializer


