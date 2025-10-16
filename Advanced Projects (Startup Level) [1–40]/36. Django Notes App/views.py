from django.shortcuts import render, redirect
from .models import Note

def home(request):
    if request.method == "POST":
        Note.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
    return render(request, "home.html", {"notes": Note.objects.all()})
