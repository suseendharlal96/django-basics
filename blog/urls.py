from django.urls import path

from .views import list_view, detail_view

urlpatterns = [
    path('', list_view, name="blog list"),
    path('detail', detail_view, name="blog detail")
]
