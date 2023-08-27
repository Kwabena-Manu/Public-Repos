from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport,on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"



class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    gender = models.CharField(max_length=1,null=True)
    flights = models.ManyToManyField(Flight, verbose_name=("flights"), blank=True, related_name='passengers')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
@receiver(post_save, sender=User)
def create_user_passenger(sender,instance,created ,**kwargs):
    if created:
        Passenger.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_user_passenger(sender,instance, **kwargs):
    instance.passenger.save()
    

    



        
    
        
    
