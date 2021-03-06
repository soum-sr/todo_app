from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
# Create your views here.


def home(request):
    tasks = Task.objects.all()

    context = {'tasks':tasks}
    return render(request, 'todo_app/home.html', context)

def createTask(request):
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            print("Form valid ")
            form.save()
            messages.success(request, 'Task Added')
        return redirect('/')

    context = {'form':form}
    return render(request, 'todo_app/create_task.html', context)
    



def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    # Prefill the form with instance
    form = TaskForm(instance=task)
    context = {'form':form}

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')


    return render(request, 'todo_app/update_task.html',context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'todo_app/delete.html', context)
