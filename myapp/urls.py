from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('hello/<str:username>',views.hello,name="hello"),
    path('projects/',views.projects,name="projects"),
    path('tasks/',views.tasks,name="tasks"),
    path('create_task/',views.create_new_task,name="create_task"),
    path('create_project/',views.create_new_project,name="create_project"),
    path('project_details/<int:id>',views.project_details,name="project_details")
]