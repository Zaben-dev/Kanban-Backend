from kanban.models import *
from kanban.serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters  import rest_framework as filters
from rest_framework.permissions import IsAuthenticated

class TasksFilter(filters.FilterSet):
    id = filters.CharFilter(lookup_expr='icontains')
    title = filters.CharFilter(lookup_expr='icontains')
    description = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Tasks
        fields = ('id','title', 'description')


class TasksViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filterset_class = TasksFilter


    @action(methods=['get'],detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('title').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class ColumnsViewSet(viewsets.ModelViewSet):
    queryset = Columns.objects.all()
    serializer_class = ColumnsSerializer
