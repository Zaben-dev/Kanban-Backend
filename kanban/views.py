from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<b>Hello, world. You're at the kanban index.</b> ")
