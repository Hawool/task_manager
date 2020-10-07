from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


def index(request):
    """Home page of Task manager"""
    return render(request, 'tasks/index.html')


@login_required
def tasks(request):
    """Output task list"""
    tasks = Task.objects.filter(owner=request.user).order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


@login_required
def new_task(request):
    """Defines a new task"""
    if request.method != 'POST':
        # No data has been sent, an empty form is created
        form = TaskForm()
    else:
        # Data was sent, process data
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return HttpResponseRedirect(reverse('tasks:tasks'))

    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


@login_required
def edit_task(request, task_id):
    """Editing a task"""
    task = Task.objects.get(id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tasks:tasks'))
    context = {'task': task, 'form': form}
    return render(request, 'tasks/edit_task.html', context)


@login_required
def delete_task(request, task_id):
    """Delete function"""
    try:
        task = Task.objects.get(id=task_id)
        task.delete()
        return HttpResponseRedirect(reverse('tasks:tasks'))
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Task not found</h2>")


@login_required
def stat_new(request):
    """Output new tasks"""
    tasks = Task.objects.filter(owner=request.user).order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/stat_new.html', context)


@login_required
def stat_planned(request):
    """Output planned tasks"""
    tasks = Task.objects.filter(owner=request.user).order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/stat_planned.html', context)


@login_required
def stat_in_hand(request):
    """Output tasks in hand"""
    tasks = Task.objects.filter(owner=request.user).order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/stat_in_hand.html', context)


@login_required
def stat_completed(request):
    """Output completed tasks"""
    tasks = Task.objects.filter(owner=request.user).order_by('date_added')
    context = {'tasks': tasks}
    return render(request, 'tasks/stat_completed.html', context)


@login_required
def time_filter(request):
    """Output filtered tasks"""
    tasks = Task.objects.filter(owner=request.user).order_by('date_planned')
    context = {'tasks': tasks}
    return render(request, 'tasks/time_filter.html', context)
