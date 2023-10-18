from django.shortcuts import render
from django.http import HttpResponse
from Gadgets.models import Item

# Create your views here.

def index(request):
    itemlist = Item.objects.all()

    context = {
        'itemlist' : itemlist
    }

    return render(request , 'Gadgets/index.html', context)


def detail(request , item_id):
    item = Item.objects.get(pk=item_id)

    context = {
        'item' : item
    }

    return render(request , 'Gadgets/detail.html', context)
