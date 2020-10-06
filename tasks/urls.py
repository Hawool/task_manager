"""Url for tasks"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Output all tasks
    path('tasks/', views.tasks, name='tasks'),
    # Page for new task
    path('new_task/', views.new_task, name='new_task'),
    # Page for editing a task
    path('edit_task/<task_id>/', views.edit_task, name='edit_task'),
    # Page for deleting a task
    path('delete_task/<task_id>/', views.delete_task, name='delete_task'),
    # Page for new tasks
    path('tasks/new/', views.stat_new, name='stat_new'),
    # Page for planned tasks
    path('tasks/planned/', views.stat_planned, name='stat_planned'),
    # Page for tasks in hand
    path('tasks/in_hand/', views.stat_in_hand, name='stat_in_hand'),
    # Page for completed tasks
    path('tasks/completed/', views.stat_completed, name='stat_completed'),

]