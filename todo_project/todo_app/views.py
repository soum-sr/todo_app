from django.shortcuts import render
from .models import Task
from .forms import TaskForm
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()

    context = {'tasks':tasks,'form':form}
    return render(request, 'todo_app/home.html', context)