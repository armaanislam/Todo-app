from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print(form.fields)
            form.save()
        return redirect('/')

    dict = {'tasks':tasks, 'form':form}
    return render(request, 'todolist/tasks.html', dict)


def updateTask(request, pk):
    task = Task.objects.get(id=pk) #Using id we can get the selected object

    form = TaskUpdateForm(instance = task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect('/')

    dict = {'form': form}
    return render(request, 'todolist/update_tasks.html', dict)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk) #Using id we can get the selected object

    if request.method == 'POST':
        #item = Task.objects.get(id=pk)
        item.delete()
        return redirect('/')

    dict = {'item': item}
    return render(request, 'todolist/delete.html', dict)