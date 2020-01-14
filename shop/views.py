from urllib import request
from datetime import datetime
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

from shop.models import Item , OrderItem, Order


def home(request):
    items_list = Item.objects.all()
    paginator = Paginator(items_list, 4)
    page_number = request.GET.get('page')

    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context={
        "items": items, 'paginate' : True
    }
    return render(request, 'home.html', context)

def product(request,id):
    item = Item.objects.get(id=id)
    context ={
        'item': item
    }
    return render(request, 'product.html', context)


def addtocard(request,id):
    item = Item.objects.get(id=id)
    #order_item = OrderItem.objects.get_or_create(item=item, user=request.user,ordered = False)

    if OrderItem.objects.filter(item=item, user=request.user, ordered=False):
        order_item = OrderItem.objects.get(item=item, user=request.user, ordered=False)
        order_item.quantity +=1
        order_item.save()

    else:
        order_item = OrderItem.objects.create(item=item, user=request.user, ordered=False)

    if Order.objects.filter(user=request.user, ordered = False):
        orders = Order.objects.filter(user=request.user, ordered=False)
        orders[0].items.add(order_item)

    else:
        order =  Order.objects.create(user=request.user, ordered=False)
        order.items.add(order_item)

    return redirect('home')


def removefromcard(request,id):
    orderitem= OrderItem.objects.filter(id=id, user=request.user)
    orderitem.delete()

    return redirect('displaycard')


def displaycard(request):
    id= request.user.id
    if Order.objects.filter(user=id, ordered=False).first():
        order = Order.objects.filter(user = id,ordered = False).first()
        order_items = order.items.all()
        total = 0
        for order_item in order_items:
            total += order_item.item.price * order_item.quantity

        context={
            'order': order,
            'order_items' : order_items,
            'total' : total
        }

        return render(request,'displaycard.html',context)
    else:
        return redirect('home')


def displaycardid(request,id):
    if Order.objects.get(id=id):
        order =  Order.objects.get(id=id)
        order_items = order.items.all()
        total = 0
        for order_item in order_items:
            total += order_item.item.price * order_item.quantity

        context={
            'order': order,
            'order_items' : order_items,
            'total' : total
        }

        return render(request,'displaycard.html',context)
    else:
        return redirect('home')


def paiement(request):
    id= request.user.id
    order = Order.objects.filter(user = id, ordered = False)[0]
    order.ordered = True
    order.ordered_date = datetime.now()
    items = order.items.all()
    total = 0
    for item in items:
        total += item.item.price * item.quantity
    order.total = total
    order.save()
    context={
        'total' : total
    }

    return redirect('displayallcards')


def displayallcards(request):
    id = request.user.id
    orders = Order.objects.filter(user = id).order_by('ordered_date')
    context={
        'orders' : orders
    }

    return render(request,'displayallcards.html',context)


def essai(request):
    items_list = Item.objects.all()
    paginator = Paginator(items_list, 4)
    page_number = request.GET.get('page')

    try:
        items = paginator.get_page(page_number)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context={
        "items": items, 'paginate' : True
    }
    return render(request, 'essai.html', context)


def homecat(request,cat):
    items_list = Item.objects.filter(category = cat).all()
    paginator = Paginator(items_list, 4)
    page_number = request.GET.get('page')

    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context={
        "items": items, 'paginate' : True
    }

    return render(request, 'homecat.html' , context)




