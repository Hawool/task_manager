"""Url for tasks"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Output all tasks
    path('tasks/', views.tasks, name='tasks'),
    # Page with detailed information of the task
    path('tasks/<task_id>/', views.task, name='task'),
    # Page for new task
    path('new_task/', views.new_task, name='new_task'),
]