from django.urls import path
from kanban import views

urlpatterns = [
    path("", views.home, name="home"),
]