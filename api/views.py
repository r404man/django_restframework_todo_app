from api.models import Task
from django.http.response import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TaskSerializers
from .models import Task
from api import serializers

@api_view(['GET'])
def ApiOverview(request):

    api_urls = {
        'List':'/task-list/',
        'Detail':'/task-detail/<str:id>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:id>',
        'Delete':'/task-delete/<str:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def TaskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializers(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TaskDetail(request, pk):
    print(pk)
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def TaskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializers(instance=task, data = request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def TaskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response(serializer.data)