from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
# Create your views here.

def time_display(request):
    context = {
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime())
    }

    return render(request,'display.html', context)