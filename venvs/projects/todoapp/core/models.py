from django.db import models


# Create your models here.

class Doctor(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    d_name = models.CharField(max_length=200, null=True, blank=False, verbose_name='Full Name')
    gender = models.CharField(max_length=200, null=True, blank=False, verbose_name='Gender', choices=gender_choices)

    def __str__(self):
        return self.d_name

class Patient(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    d_name = models.CharField(max_length=200, null=True, blank=False, verbose_name='Full Name')
    gender = models.CharField(max_length=200, null=True, blank=False, verbose_name='Gender', choices=gender_choices)
    p_d_Details = models.ManyToManyField(Doctor, blank=False, verbose_name="Choose Doctor")

    def __str__(self):
        return self.d_name

# todo list
class Task(models.Model):
    taskId = models.AutoField(primary_key=True)
    task = models.CharField(max_length=1500, null=True, blank=False, verbose_name='Add your task')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.task} - {self.start_date}"