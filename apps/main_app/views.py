from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *


def index(request):
    return  render(request, "landing_page.html")

def inquiry(request):

    form = RescueeForm()

    if request.method == 'POST':
        form = RescueeForm(request.POST)
        if form.is_valid():
            rescuee_instance = form.save()
        return redirect ('rescuee', rescuee_instance.pk)

    context = {
        'form' : form
    }

    return render(request, "inquiry_page.html", context)

def rescueeview(request, pk):

    rescuee = Rescuee.objects.get(id=pk)

    print(rescuee.name)
    print(rescuee.disaster)

    context = {
    'rescuee' : rescuee,
    }

    return render(request, "rescuee_page.html", context)

def rescue_dashboard(request):

    all = Rescuee.objects.all()

    context = {
    'all' : all,
    }

    return render(request, "rescuers_page.html", context)
