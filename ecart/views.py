from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import auth

from .models import Destination


# def index(request):
#     obj1 = {'id': 1,
#             "name": "madurai",
#             "price": "800",
#             "img": "destination_4.jpg",
#             "description": "City of Temple",
#             "offer":True
#             }
#     obj2 = {'id': 2,
#             "name": "chennai",
#             "price": "1000",
#             "img": "destination_5.jpg",
#             "description": "Beach",
#             "offer":False
#             }
#     obj3 = {'id': 3,
#             "name": "USA",
#             "price": "1500",
#             "img": "destination_6.jpg",
#             "description": "City of Dreams",
#             "offer":False
#             }
#     dest1 = Destination()
#     dest1.dest(obj1)
#     dest2 = Destination()
#     dest2.dest(obj2)
#     dest3 = Destination()
#     dest3.dest(obj3)
#     dests = [
#         dest1,
#         dest2,
#         dest3
#     ]

# With DB:

def index(request):

    dests = Destination.objects.all()
    # print(dests[0].img)
    context = {
        "dests": dests
    }
    return render(request, 'index.html', context)


def single_destination_view(request, place):
    # 1st approach
    # dest = Destination.objects.get(name=place.capitalize())

    # 2nd approach(to check wheather it exists or 404 page)
    dest = get_object_or_404(Destination,  name=place.capitalize())
    context = {
        "dest": dest
    }
    return render(request, 'destination.html', context)
