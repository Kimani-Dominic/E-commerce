from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from  django.http import JsonResponse

from .models import *

#from .forms import UserCreationForm

# Create your views here.
def store(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'Errands/store.html', {'products': products})

def cart(request):
    
    if request.user.is_authenticated:
       customer = request.user.customer
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
           
       
    context = {'items':items, 'order':order}
    return render(request, 'Errands/cart.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
       customer = request.user.customer
       order, created = Order.objects.get_or_create(customer=customer, complete=False)
       items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    
    context = {}
    return render(request, 'Errands/checkout.html', context)

def LoginPage(request):
    context = {}
    return render(request, 'Errands/login.html', context)

def registerPage(request):
    form = UserCreationForm()
    
    if request.method  == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'Errands/register.html', context)


def UpdateItem(request):
    return JsonRespose('item was added', safe=False)