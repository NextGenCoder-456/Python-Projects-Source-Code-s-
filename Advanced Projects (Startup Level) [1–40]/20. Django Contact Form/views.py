from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'thanks.html')
    return render(request, 'contact.html', {'form': form})
