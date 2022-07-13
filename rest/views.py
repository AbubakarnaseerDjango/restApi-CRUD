from asyncio import tasks
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import TaskSerializers
from . models import Task
from rest import serializers
# Create your views here.
@api_view(['GET'])
def restview (request):
       lista = {
         'dskdk':'sdsd',
         'sdsdsd':'sdsd',
            
       }

       return Response(lista)
@api_view(['GET'])
def seriview (request):
    tasks = Task.objects.all()
    serializer  = TaskSerializers(tasks, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create (request):
  serializer  = TaskSerializers(data = request.data)
  if serializer.is_valid():
      serializer.save()
  return Response (serializer.data)