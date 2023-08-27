from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

# class Topping(models.Model):
#     """Add Toppings to define a Pizza Type"""


#     On = 'Onion'
#     Bf = 'Beef'
#     Chk = 'Chicken'
#     Veg = 'Vegetables'

#     toppings_choices = [
#         (On,'Onion'),
#         (Bf,'Beef'),
#         (Chk,'Chicken'),
#         (Veg, 'Vegetables')
#     ]

#     name = models.CharField(max_length=50,choices=toppings_choices,default=On)
    
#     def __str__(self):
#         return self.name


class Pizza(models.Model):
    """Make Pizza for a customer"""

    On = 'Onion'
    Bf = 'Beef'
    Chk = 'Chicken'
    Veg = 'Vegetables'

    toppings_choices = [
        (On,'Onion'),
        (Bf,'Beef'),
        (Chk,'Chicken'),
        (Veg, 'Vegetables')
    ]


    name = models.CharField(max_length=50)  
    toppings = MultiSelectField(choices=toppings_choices,null=True)
    

    
    
    class Meta:
        verbose_name_plural = 'pizza' 

    def __str__(self):
        return self.name



    
    

class Order(models.Model):
    """Make an Order"""

    sm ='small'
    med ='medium'
    lar ='large'
    xl ='extra large'

    size_choices = [
        (sm,'small'),
        (med,'medium'),
        (lar,'large'),
        (xl,'extra large')
    ]

    name_of_orderer = models.CharField(max_length=50,null=True)
    pizza = models.ForeignKey(Pizza,on_delete=models.SET_NULL, null=True)
    size = models.CharField(max_length=50,choices=size_choices, default=sm)

    def __str__(self):
        return f"{self.name_of_orderer}'s order , {self.pizza} , {self.size}"
