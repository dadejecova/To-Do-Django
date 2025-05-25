from django.shortcuts import render
from todo.models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-created_at')

    completed_task =  Task.objects.filter(is_completed=True).order_by('-created_at')
    context = {
        'tasks': tasks,
        'completed_task': completed_task,

    }   
    return render(request, 'home.html', context)