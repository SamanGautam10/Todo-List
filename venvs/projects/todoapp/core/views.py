from django.shortcuts import render
from django.http import HttpResponse
from core.models import *

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
        return render(request=request, template_name='todolist.html')
    
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