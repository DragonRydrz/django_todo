from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world! You're at the todo index!")


def list(request):
    return HttpResponse("You have reached the list of ToDos!")


def item(request, todo_id):
    return HttpResponse("This is the task with an id of %s" % todo_id)
