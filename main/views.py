from django.shortcuts import render,redirect
from .models import task
from .forms import taskForm
import os
# Create your views here.

def home(request):
    tasks = task.objects.all()
    form = taskForm()
    if request.method == 'POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    LOWcolor = "green"
    MEDIUMcolor = "yellow"
    HIGHcolor = "red"
    context = {
        'tasks': tasks,
        'LOWcolor' : "green",
        'MEDIUMcolor' : "yellow",
        'HIGHcolor' : "red",
        'form': form,
    }
    return render(request, 'main/home.html', context)

def complete_task(request):
    return render(request, 'main/complete_task.html')

def create_task(request):
    form = taskForm()

    if request.method == 'POST':
        form = taskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'main/create.html', context)

def edit_task(request, pk):
    tasks = task.objects.get(id=pk)
    form = taskForm(instance=tasks)

    if request.method == 'POST':
        form = taskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'main/edit.html', context)


def delete_task(request, pk):
    tasks = task.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    context = {
        'tasks': tasks,
    }
    return render(request, 'main/delete.html', context)