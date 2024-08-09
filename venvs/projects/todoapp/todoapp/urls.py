"""
URL configuration for todoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="homepage"),
    path("all/patient", get_all_patient, name="all_patient"),
    path("todo-list", todo_list, name="todo_list"),
    path("save/task", save_todo_list, name="save_task"),

    # url to import task list from database to html page
    path("todo-list-tasks", import_task, name="import_task"),

    # url for delete function
    path("delete/task/<int:taskId>", delete_task, name="delete_task"),  # sending taskId to views

    # testing forms.py of django
    path("form/task", form_task, name="form_task"),

    # url path for edit task functions
    path("edit/task/<int:taskId>/", update, name="task_list"), 
    path("edit/save_edit/<int:taskId>/", update_save, name="update_save"),
]
