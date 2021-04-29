from rest_framework.authentication import SessionAuthentication

from ..serializers import *
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication


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
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

class ColumnsViewSet(viewsets.ModelViewSet):
    queryset = Columns.objects.all()
    serializer_class = ColumnsSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class RowsViewSet(viewsets.ModelViewSet):
    queryset = Rows.objects.all()
    serializer_class = RowsSerializer


# class CellsViewSet(viewsets.ModelViewSet):
#     queryset = Cells.objects.all()
#     serializer_class = CellsSerializer


