
from django.shortcuts import render
from todo.models import Task

def home(request):
    task = Task.objects.filter(is_completed =False).order_by('-updated_at')
    Ctasks = Task.objects.filter(is_completed = True)
    context = {
        'task123': task,
        'completed_tasks': Ctasks,
    }
    return render(request,'home.html', context)
