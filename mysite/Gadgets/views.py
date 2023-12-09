from django.shortcuts import render , redirect
from django.http import HttpResponse
from Gadgets.models import Item
from Gadgets.forms import ItemForm
from Gadgets.models import History
from users.models import CusOrders , CusRatingFeedback

# Create your views here.

def index(request):
    
    if request.user.is_superuser:
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user=request.user.username)

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    else:
        itemlist = Item.objects.all()
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    context = {
        'itemlist' : itemlist
    }

    return render(request , 'Gadgets/index.html', context)


def detail(request , item_id):
    item = Item.objects.get(pk=item_id)

    hist = History.objects.filter(
        prod_ref = item.prod_code
    )

    # Restaurant and Admin

    if request.user.profile.user_type == 'Rest' or request.user.profile.user_type == 'Admin':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code
        )

    # Customer
    
    elif request.user.profile.user_type == 'Cust':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code , 
            user = request.user.username
        )

    crf = CusRatingFeedback.objects.filter(
        prod_code = item.prod_code
    )

    context = {
        'item' : item,
        'hist' : hist,
        'oco'  : Obj_CusOrd,
        'crf'  : crf
    }

    return render(request , 'Gadgets/detail.html', context)


def allproduct(request):

    if request.user.is_superuser:
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    elif request.user.is_authenticated and request.user.profile.user_type == 'Rest':
        itemlist = Item.objects.filter(for_user=request.user.username)

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    elif request.user.is_authenticated and request.user.profile.user_type == 'Cust':
        itemlist = Item.objects.all()

        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains = item_name )

    else:
        itemlist = Item.objects.all()

    context = {
        'itemlist' : itemlist
    }

    return render(request , 'Gadgets/allproduct.html' , context)

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


def category(request, val):

    items = Item.objects.filter(
        category = val
    )


    context = {
        'items':items
    }
    
    return render(request, 'Gadgets/category.html',context)
