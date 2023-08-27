from django.shortcuts import render
from .models import Pizza
from .forms import OrderForm
from django.shortcuts import redirect

from django.http import HttpResponse
import time



# Create your views here.

def index(request):
    """The homepage of Kwabena's Pizza"""
    return render(request,'pizzeria_app/index.html')


def pizzas(request):
    """Display the types of Pizza available"""

    pizzas = Pizza.objects.all()

    context = {'pizzas': pizzas}

    return render(request,'pizzeria_app/pizzas.html',context)

def pizza(request,pizza_id):
    """Display the information for a Pizza like orders and toppings"""
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.toppings

    orders = pizza.order_set.all()

    num_of_orders = len(orders)

    context = {'pizza':pizza, 'toppings': toppings, 'orders': orders,'num_of_orders': num_of_orders}



    return render(request,'pizzeria_app/pizza_page.html',context)



def new_order(request,pizza_id):
    pizza_order = Pizza.objects.get(id=pizza_id)
    
    if request.method != 'POST':
        order_form = OrderForm()

    else:
        order_form = OrderForm(data=request.POST)
        if order_form.is_valid:
            saved_order = order_form.save(commit=False)
            saved_order.pizza = pizza_order
            saved_order.save()
            HttpResponse("<h1>Contgrats you've made an Order for {{pizza}}<h1>")
            time.sleep(5)
        
           
            return redirect('pizzeria_app:pizza',pizza_id=pizza_id)


    context = {'pizza': pizza_order, 'form': OrderForm}
    return render(request,'pizzeria_app/new_order.html',context)



