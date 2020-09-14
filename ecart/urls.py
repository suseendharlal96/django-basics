from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="ecart"),
    path('destination/<str:place>',views.single_destination_view,name='destination')
]
