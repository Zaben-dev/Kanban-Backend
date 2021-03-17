from django.views.generic import ListView, DetailView
from .serializers import *


class TasksListView(ListView):
    model = Tasks
    template_name = 'kanban/kanban_list.html'


class TasksDetailView(DetailView):
    model = Tasks
    template_name = 'kanban/kanban_detail.html'


class ColumnsListView(ListView):
    model = Columns
    template_name = 'kanban/kanban_list.html'


class ColumnsDetailView(DetailView):
    model = Columns
    template_name = 'kanban/kanban_detail.html'

