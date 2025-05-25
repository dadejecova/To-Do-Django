from django.shortcuts import render
from todo.models import Task
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False)
    context = {
        'tasks': tasks
    }   
    return render(request, 'home.html', context)