from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        if len(request.POST.get('num1')) > 0 and len(request.POST.get('num2')) > 0:
            result = int(request.POST.get('num1')) + \
                int(request.POST.get('num2'))
        else:
            result = "enter a value"
        return render(request, 'calc.html', {"result": result})
    else:
        return render(request, 'calc.html', {"name": "susee"})


