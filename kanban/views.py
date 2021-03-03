from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TaskListView(ListView):
    model = Task
    template_name = 'kanban/kanban_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'kanban/kanban_detail.html'


class ColumnListView(ListView):
    model = Column
    template_name = 'kanban/kanban_list.html'


class ColumnDetailView(DetailView):
    model = Column
    template_name = 'kanban/kanban_detail.html'

