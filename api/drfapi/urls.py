from django.urls import path, include
from .views import hello,tasks,task
from .views import TaskList, TaskDetail, TaskViewSet, AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('hello/', hello),
    # path('tasks/', tasks),
    # path('tasks/<int:pk>/', task),

    # path('tasks/', TaskList.as_view()),
    # path('tasks/<int:pk>/', TaskDetail.as_view()),
]

routers = DefaultRouter()
routers.register('tasksSet', TaskViewSet, basename='tasksSet')
routers.register('authors', AuthorViewSet, basename='authors')
routers.register('books', BookViewSet, basename='books')
urlpatterns += routers.urls