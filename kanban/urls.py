from django.urls import path
from . import views

app_name = 'kanban'
urlpatterns = [
    path('', views.TasksListView.as_view(), name='list'),
    path('<int:pk>/', views.TasksDetailView.as_view(), name='detail'),
    path('', views.ColumnsListView.as_view(), name='list'),
    path('<int:pk>/', views.ColumnsDetailView.as_view(), name='detail'),
    path('', views.RowsListView.as_view(), name='list'),
    path('<int:pk>/', views.RowsDetailView.as_view(), name='detail'),
    # path('', views.CellsListView.as_view(), name='list'),
    # path('<int:pk>/', views.CellsDetailView.as_view(), name='detail'),
    path('users', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
]
