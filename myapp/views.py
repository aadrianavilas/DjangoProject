from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Task, Project
from .forms import CreateNewTask,CreateNewProject

# Create your views here.


def index(request):
    title='DJANGO COURSE'
    return render(request,'index.html',{
        'title':title
    })

def about(request):
    username='aadrianavilas'
    return render(request,'about.html',{
        'username':username
    })

def hello(request,username):
    return HttpResponse("<h1>Hello, %s </h1>" %username)
    
def projects(request):
    # projects=list(Project.objects.values())
    projects=Project.objects.all()
    return render(request,'projects/projects.html',{
        'projects':projects
    })

def tasks(request):
    tasks=Task.objects.all()
    return render(request,'tasks/tasks.html',{
        'tasks':tasks
    })

def create_new_task(request):
    if request.method=='GET':   
        return render(request,'tasks/create_task.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=1)
        return redirect('tasks')


def create_new_project(request):
    if request.method=='GET':
        return render(request,'projects/create_project.html',{
            'form':CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_details(request,id):
    project=get_object_or_404(Project,id=id)
    tasks=Task.objects.filter(project_id=id)
    return render(request,'projects/projects_details.html',{
        'project':project,
        'tasks':tasks
    })
    