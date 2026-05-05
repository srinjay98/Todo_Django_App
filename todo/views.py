from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone 
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
# Create your views here.

def register(request):
    # if request.method == 'POST' :
        # username = request.POST['username']
        # password = request.POST['password']

        # user = User.objects.create_user(username = username, password = password)
        # login(request, user)
        # return redirect('task_list')
    #  return render(request, 'register.html')    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 🔐 hash password
            user.save()

            login(request, user)
            return redirect('task_list')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})    

def user_login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user:
          
          login(request, user)
          return redirect('task_list')
    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    return render(request, 'task_list.html', {'tasks':tasks})

@login_required
def create_task(request) :
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(user=request.user, title = title)
        return redirect('task_list')
    return render(request, 'create_task.html')

@login_required
def update_task(request, id):
    task = get_object_or_404(Task, id=id, user = request.user) 
    if request.method == 'POST':
        task.title = request.POST['title']   
        task.save()
        return redirect('task_list')
    return render(request, 'update_task.html', {'task':task})

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user = request.user)
    task.delete()
    return redirect('task_list')

@login_required
def complete_task(request, id):

    task = get_object_or_404(Task, id=id, user = request.user)

    task.complete = True
    task.completed_at = timezone.now()
    task.save()

    print("Completed Status:", task.complete)
    print("Completed Time:", task.completed_at)

    return redirect('task_list')
    # return redirect('/')



