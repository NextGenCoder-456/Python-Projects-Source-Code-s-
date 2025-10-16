from django.shortcuts import render, redirect
from .models import Message

def chatroom(request):
    if request.method == "POST":
        Message.objects.create(
            username=request.POST['user'],
            content=request.POST['msg']
        )
    return render(request, "chat.html", {"messages": Message.objects.all()})
