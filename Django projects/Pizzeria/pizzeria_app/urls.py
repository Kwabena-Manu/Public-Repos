from django.urls import path
from . import views


app_name = 'pizzeria_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas/',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),
    path('pizzas/<int:pizza_id>/new_order',views.new_order,name='new_order')
]

