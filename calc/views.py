from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'calc.html', {"name": "susee"})


def add(request):
    if len(request.POST.get('num1')) > 0 and len(request.POST.get('num2')) > 0:
        result = int(request.POST.get('num1')) + int(request.POST.get('num2'))
    else:
        result = "enter a value"
    return render(request, 'index.html', {"result": result})
