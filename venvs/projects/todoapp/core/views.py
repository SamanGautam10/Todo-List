from django.shortcuts import render
from core.models import *

# Create your views here.
def home(request):
    return render(request=request, template_name='index.html')

def get_all_patient(request):
    details = Patient.objects.all()

    context = {
        'details': details
    }

    return render(request=request, template_name='patient.html', context=context)