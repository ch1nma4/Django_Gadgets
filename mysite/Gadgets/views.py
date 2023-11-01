from django.shortcuts import render , redirect
from django.http import HttpResponse
from Gadgets.models import Item
from Gadgets.forms import ItemForm
from Gadgets.models import History

# Create your views here.

def index(request):
    
    if request.user.is_superuser:
        itemlist = Item.objects.all()

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user=request.user.username)

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()

    else:
        itemlist = Item.objects.all()

    context = {
        'itemlist' : itemlist
    }

    return render(request , 'Gadgets/index.html', context)


def detail(request , item_id):
    item = Item.objects.get(pk=item_id)

    hist = History.objects.filter(
        prod_ref = item.prod_code
    )

    context = {
        'item' : item,
        'hist' : hist
    }

    return render(request , 'Gadgets/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()

        Obj_History = History(

            user_name = request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = request.POST.get('item_name'),
            op_type = 'Created'
        )

        Obj_History.save()


        return redirect('Gadgets:index')
    
    context = {
        'form': form
    }
    
    return render(request , 'Gadgets/item-form.html' , context)


def update_item(request , id):
    item = Item.objects.get(pk = id)
    form = ItemForm(request.POST or None , instance=item)

    if form.is_valid():
        form.save()

        Obj_History = History(

            user_name = request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = request.POST.get('item_name'),
            op_type = 'Updated'
        )

        Obj_History.save()

        return redirect('Gadgets:index')

    context = {
        'form' : form,
    }

    return render(request , 'Gadgets/item-form.html' , context)

def delete_item(request , id):
    item = Item.objects.get(pk = id)

    context = {
        'item' : item
    }

    if request.method == 'POST':
        item.delete()

        Obj_History = History(

            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = item.item_name,
            op_type = 'Deleted'
        )

        Obj_History.save()

        return redirect('Gadgets:index')
    

    return render(request , 'Gadgets/item-delete.html' , context)
