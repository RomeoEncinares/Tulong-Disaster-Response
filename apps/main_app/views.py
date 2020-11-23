from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *


def index(request):
    return  render(request, "landing_page.html")

def inquiry(request):

    form = RescueeForm()

    context = {
        'form' : form
    }

    return render(request, "inquiry_page.html", context)
