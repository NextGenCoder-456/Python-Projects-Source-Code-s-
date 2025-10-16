from django.shortcuts import render, redirect
from .models import Poll, Option

def poll_view(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == "POST":
        selected = request.POST['option']
        option = Option.objects.get(id=selected)
        option.votes += 1
        option.save()
        return redirect('results', poll_id=poll.id)
    return render(request, "poll.html", {"poll": poll})
