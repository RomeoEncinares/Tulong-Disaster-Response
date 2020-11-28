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

    context = {
    'rescuee' : rescuee,
    }

    return render(request, "rescuee_page.html", context)

def rescue_dashboard(request):

    all = Rescuee.objects.all()
    going = Rescuee.objects.filter(status="Going")
    waiting = Rescuee.objects.filter(status="Waiting")

    goingcount = going.count()
    waitingcount = waiting.count()

    context = {
    'all' : all,
    'going' : going,
    'waiting' : waiting,
    'goingcount' : goingcount,
    'waitingcount' : waitingcount,
    }

    return render(request, "rescuers_page.html", context)

def rescuer_info(request, pk):

    rescuee = Rescuee.objects.get(id=pk)
    form = RescueeForm(instance=rescuee)

    if request.method == 'POST':
        form = RescueeForm(request.POST, request.FILES, instance=rescuee)
        if form.is_valid():
            form.save()
        return redirect ('../')

    context = {
    'rescuee' : rescuee,
    'form': form,
    }

    return render(request, "information-rescuer.html", context)

def done_rescue(request, pk):
    rescuee = Rescuee.objects.get(id=pk)

    if request.method == 'POST':
        rescuee.delete()
        return redirect ('../')

    context = {
    'rescuee' : rescuee,
    }

    return render(request, "done-rescue.html", context)
