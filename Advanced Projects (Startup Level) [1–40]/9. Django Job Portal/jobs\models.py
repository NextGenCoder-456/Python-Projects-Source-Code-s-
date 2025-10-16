from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    posted_on = models.DateField(auto_now_add=True)

# jobs/views.py
from django.shortcuts import render
from .models import Job

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

# jobs/urls.py
from django.urls import path
from .views import job_list

urlpatterns = [
    path('', job_list, name='job_list'),
]
