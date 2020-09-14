from django.shortcuts import render

# Create your views here.


def list_view(request):
    return render(request, 'article_list.html', {})


def detail_view(request):
    return render(request, 'article_detail.html', {})
