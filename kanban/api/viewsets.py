from kanban.models import *
from kanban.serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters  import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

class TaskFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ('title', 'description')


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter


    @action(methods=['get'],detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('title').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
