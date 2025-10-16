from django.shortcuts import render
from .models import Upload

def upload_file(request):
    if request.method == "POST":
        Upload.objects.create(file=request.FILES['file'])
    return render(request, "upload.html", {"files": Upload.objects.all()})
