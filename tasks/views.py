from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm


def index(request):
    """Home page of Task manager"""
    return render(request, 'tasks/index.html')


def tasks(request):
    """Output task list"""
    tasks = Task.objects.order_by('date_added')
    # task = Task.objects.get(id=task_id)
    # entry = task.entry_set
    # context = {'tasks': tasks, 'entry': entry}
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


def task(request, task_id):
    """Show one task with entry"""
    task = Task.objects.get(id=task_id)
    entries = task.entry_set
    context = {'task': task, 'entries': entries}
    return render(request, 'tasks/task.html', context)


def new_task(request):
    """Defines a new topic"""
    if request.method != 'POST':
        # No data has been sent, an empty form is created
        form = TaskForm()
    else:
        # Data was sent, process data
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:tasks'))

    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)