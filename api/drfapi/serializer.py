from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from drfapi.models import *

class TaskSerializer(ModelSerializer):  
    class Meta:
        model = Task    
        fields = '__all__'

        
class BookSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Book
        fields = ['id', 'title', 'price', 'author']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta: 
        model = Author
        fields = ['id', 'name', 'bio', 'books',]