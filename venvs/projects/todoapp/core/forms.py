from core.models import *

from django import forms

class addTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"