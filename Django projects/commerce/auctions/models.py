from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


    



class User(AbstractUser):
    watchlist = models.ManyToManyField('Listings', verbose_name=("watchlists"),related_name='watchlist')

    class Meta:
        verbose_name_plural ="Users"
    def __str__(self):
        return self.username
    

class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    



class Listings(models.Model):
    user = models.ForeignKey(User, verbose_name=("users"), on_delete=models.CASCADE,related_name="listings")
    title = models.CharField(max_length=64)
    description = models.CharField( max_length=150)
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    listing_pic = models.ImageField(upload_to='photos/%Y/%m/%d', height_field=None, width_field=None, max_length=100,null=True,blank=True)
    category = models.CharField(max_length=64,null=True,blank=True)
    winner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="won_listings")

    date_added = models.DateTimeField(auto_now_add=True,auto_now=False)

    class Meta:
        verbose_name_plural = 'Listings'


    def __str__(self):
        return self.title

    
       

class Bids(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE,related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bids')
    bid = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Bids'

    def __str__(self):
        return f"{self.listing} : {self.bid} by {self.user} "


class Comment(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    date_added = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    class Meta:
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f"{self.comment[:50]} ..."
    


@receiver(post_save, sender=Bids)
def change_listing_bid(sender,instance,created ,**kwargs):
    thelisting = instance.listing
    thelisting.bid = instance.bid
    thelisting.save()
        


@receiver(post_save,sender=Listings)
def add_category(sender,instance,created, **kwargs):
    if created:
        if instance.category:
            exist = False
            catlist=Category.objects.all()
            for cat in catlist:
                if instance.category.lower() == cat.name.lower():
                    exist=True
                    break

            if not exist:
                cat = Category(name=instance.category)
                cat.save()