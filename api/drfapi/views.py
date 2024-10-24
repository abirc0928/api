from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, Author, Book
from .serializer import TaskSerializer, AuthorSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
@api_view(['GET','POST'])
def hello(request):
    return Response({"hello":"world"})

# -------------------1St Method start------------------
@api_view(['GET','POST'])
def tasks(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def task(request, pk):
    try:
        task = Task.objects.get(pk=pk)  
    except Task.DoesNotExist:
        return Response(status=404) 
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)     

# -------------------1St Method end------------------

# -------------------2nd Method start------------------
class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all()      
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)    

    def post(self, request):    
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TaskDetail(APIView):

    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)  
        except Task.DoesNotExist:
            return Response(status=404) 
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = Task.objects.get(pk=pk)  
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)        
        return Response(serializer.errors, status=400)
    def delete(self, request, pk):
        task = Task.objects.get(pk=pk)  
        task.delete()
        return Response(status=204)
     
# -------------------2nd Method end------------------

# -------------------3rd Method start------------------

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer  

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# -------------------3rd Method end------------------