from django.shortcuts import render, redirect
from core.models import *
from core.forms import *


def TaskList(request):
    tasks = Task.objects.all()

    return render(request, 'core/Task.html', {"tasks": tasks})

def CreateTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'core/Task_Form.html' , context)

def UpdateTask(request, pk):

    Tasks= Task.objects.get(id=pk)
    form = TaskForm(instance=Tasks)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=Tasks)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'core/Task_Form.html', context)

def deleteTask(request,pk):
    item = Task.objects.get(id=pk)
    if request.method =='POST':
        item.delete()
        return redirect('home')

    context = {'item':item}
    return render(request, 'base/Deletetask.html' , context)