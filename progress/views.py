from django.shortcuts import render
from .models import *


# Create your views here.

def homepage(request):
    article  = news.objects.all()
    context  = {
        'article': article
    }
    return render(request, 'index.html', context)

def newsView(request, id):
    anews = news.objects.get(id=id)
    context  = {
        'anews': anews
    }
    return render(request, 'viewpage.html', context)