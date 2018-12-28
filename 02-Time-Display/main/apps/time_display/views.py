from django.shortcuts import render, redirect, HttpResponse
import datetime

# Create your views here.
def index(request):

    currentDT = datetime.datetime.now()
    dateStr = currentDT.strftime("%A, %B %d, %Y")
    timeStr = currentDT.strftime("%I:%M:%S %p")
    
    context = {
        'date'  :   dateStr,
        'time'  :   timeStr
    }

    return render(request, 'index.html', context)