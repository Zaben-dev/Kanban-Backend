from django.views.generic import ListView, DetailView
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from knox.auth import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView


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


class RowsListView(ListView):
    model = Rows
    template_name = 'kanban/kanban_list.html'


class RowsDetailView(DetailView):
    model = Rows
    template_name = 'kanban/kanban_detail.html'


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"user": UserSerializer(user,
                                                context=self.get_serializer_context()).data,
                         "token": AuthToken.objects.create(user)[1]})


class LoginAPI(KnoxLoginView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
