from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from dash.models import Progress
# Create your views here.



def index(request):
    return render(request,'index.html')


def response(request):
    # return HttpResponse('this is dashboard')
    if request.method == "POST":
        username = request.POST.get('username')
        task = request.POST.get('task')
        report = request.POST.get('report')
        progress= Progress(username=username, task=task, report=report, date= datetime.today())
        progress.save()
        messages.success(request, 'Your message sent succesfully.')


    return render(request, 'response.html')