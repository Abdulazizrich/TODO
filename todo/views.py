from django.shortcuts import render,redirect
from todo.models import *
from django.views import *
from .models import *
class Tasks(View):
    def get(self,request):
        context={
            'tasks':Task.objects.all(),
        }
        return render(request, 'index.html',context)
    def post(self,request):
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST['deadline']
        )
        return redirect('tasks')

def login(request):
    return render(request, 'login.html')
def edit(request):
    return render(request, 'edit.html')
def task_ochir(request, id):
    Task.objects.get(id=id).delete()
    return redirect("/tasks/")
def edit(request, id):
    if request.method == 'POST':
        task= Task.objects.get(id=id)
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.status = request.POST['status']
        task.save()
        return redirect('/tasks/')
    context = {
        'task': Task.objects.get(id=id),
    }
    return render(request, 'edit.html', context)