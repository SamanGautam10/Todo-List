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
