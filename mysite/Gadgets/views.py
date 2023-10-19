from django.shortcuts import render , redirect
from django.http import HttpResponse
from Gadgets.models import Item
from Gadgets.forms import ItemForm

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

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('Gadgets:index')
    
    context = {
        'form': form
    }
    
    return render(request , 'Gadgets/item-form.html' , context)

