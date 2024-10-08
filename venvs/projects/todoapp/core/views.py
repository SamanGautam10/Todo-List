from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from core.models import *
from core.forms import *
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request=request, template_name='index.html')

# extraction of patient details from database
def get_all_patient(request):
    details = Patient.objects.all()

    context = {
        'details': details
    }

    return render(request=request, template_name='patient.html', context=context)

def todo_list(request):
    return render(request=request, template_name='todolist.html')

# saving the tasks to be done given by user in database
def save_todo_list(request):
    
    # getting inserted data from form
    if request.method == "POST":
        task = request.POST.get('task')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')

        # creating taskName instance and saving in database
        taskName = Task(task = task, start_date = startdate, end_date = enddate)
        taskName.save()
        return HttpResponseRedirect(reverse('import_task')) # sending redirect to views.import_task
    
    else:
        return HttpResponse("Error inserting data")
    
# extraction of data from database
def import_task(request):
    details = Task.objects.all()

    # passing details into a dictionary
    context = {
        'details': details
    }

    return render(request=request, template_name='todolist.html', context=context)

# taking taskId as parameter to delete desired task
def delete_task(request, taskId):
    task = Task.objects.get(taskId = taskId)
    task.delete()
    # sending redirect to views.import_task after deletion of the task
    return HttpResponseRedirect(reverse('import_task')) 

# creation of form using forms.py
def form_task(request):
    s = addTask()
    if request.method == "POST":
        s = addTask(request.POST)

        if s.is_valid():
            return redirect('form_task')
    
    context = {
        's': s
    }

    return render(request=request, template_name="form.html", context=context)

# sending values to update.html file after clicking edit button
def update(request, taskId):
    task = Task.objects.get(taskId = taskId)
    context = {
        'task': task
    }
    return render(request=request, template_name="update.html", context=context)

# logic to edit existing data from database using form
def update_save(request, taskId):
    if request.method == "POST":
        task_new = request.POST.get('task')
        start_date_new = request.POST.get('startdate')
        end_date_new = request.POST.get('enddate')

        update_set = Task.objects.get(taskId = taskId)

        update_set.task = task_new
        update_set.start_date = start_date_new
        update_set.end_date = end_date_new
        update_set.save()

        return redirect('import_task')