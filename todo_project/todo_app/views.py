from django.shortcuts import render
from .models import Task
# Create your views here.


def home(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'todo_app/home.html', context)