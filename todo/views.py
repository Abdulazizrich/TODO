from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import *
from django.views import *
from .models import *


class Tasks(View):
    def get(self, request):
        context = {
            'tasks': Task.objects.filter(user=request.user),
        }
        return render(request, 'index.html', context)

    def post(self, request):
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            status=request.POST['status'],
            deadline=request.POST['deadline'],
            user=request.user
        )
        return redirect('tasks')


def edit(request):
    return render(request, 'edit.html')


def task_ochir(request, id):
        Task.objects.get(id=id).delete()
        return redirect("/tasks/")


class TaskEditView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            task = get_object_or_404(Task, id=id)
            context = {
                'task': task
            }
            return render(request, 'edit.html', context)
        return redirect('login')

    def post(self, request, id):
        task=get_object_or_404(Task, id=id)
        if request.user==task.user:
            task = Task.objects.get(id=id)
            task.title = request.POST['title']
            task.description = request.POST['description']
            task.status = request.POST['status']
            task.save()
            return redirect('/tasks/')
        return redirect('logout')






class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('tasks')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
