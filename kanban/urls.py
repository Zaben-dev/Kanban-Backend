from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'kanban'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('', views.ColumnListView.as_view(), name='list'),
    path('<int:pk>/', views.ColumnDetailView.as_view(), name='detail'),

]