from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'kanban'
urlpatterns = [
    path('', views.TasksListView.as_view(), name='list'),
    path('<int:pk>/', views.TasksDetailView.as_view(), name='detail'),
    path('', views.ColumnsListView.as_view(), name='list'),
    path('<int:pk>/', views.ColumnsDetailView.as_view(), name='detail'),
]