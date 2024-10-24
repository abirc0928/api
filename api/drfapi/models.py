from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Author(models.Model): 
    name = models.CharField(max_length=200)
    bio= models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Book(models.Model): 
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title