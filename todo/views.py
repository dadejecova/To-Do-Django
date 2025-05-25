from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(title=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')