from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserCreationForm,ListingForm,BidForm,CommentForm
from django.contrib.auth.decorators import login_required
from .models import User,Listings,Bids,Category,Comment


def index(request):
    listings = Listings.objects.filter(winner=None)
    context = {'listings':listings}
    return render(request, "auctions/index.html",context)


# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "auctions/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "auctions/login.html")


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request,new_user)
            return HttpResponseRedirect(reverse('auctions:index'))
        else:
            return render(request,'auctions/register.html',{'form': form,'message':"Obey the password rules"})

        
        


    else:
        form = UserCreationForm()
        return render(request, "auctions/register.html",{'form':form})


def listing(request,listing_id):

    listing = Listings.objects.get(id=listing_id)
    commentform  = CommentForm()
    bidform = BidForm()
    listing_bid = float(listing.bid)

        

    context = {'listing':listing,'bidform':bidform,'listing_bid':listing_bid,'commentform':commentform}
    return render(request,'auctions/listing.html',context)



@login_required
def makelistings(request):

    if request.method == "POST":
        user = request.user
        form = ListingForm(request.POST,request.FILES)

        if form.is_valid():
            Listing = form.save(commit=False)
            Listing.user = user
            Listing.save()



            return HttpResponseRedirect(reverse('auctions:listing',args=(Listing.id,)))
    form = ListingForm()
    context = {'form': form}
    return render(request,'auctions/makelistings.html',context)

    form = ListingForm()

    context = {'form': form}
    return render(request,'auctions/makelistings.html',context)



@login_required
def bid(request,listing_id):
    listing = Listings.objects.get(id=listing_id)
    is_first =True
    if request.method == 'POST':
        bidform = BidForm(request.POST)
        if len(listing.bids.all()) == 0:
            last_bid = listing.bid
            
        else:
            is_first =False
            last_bid  = listing.bids.last().bid
           

        if bidform.is_valid():
            thebid = bidform.save(commit=False)
            thebid.user = request.user
            thebid.listing = listing
            
            if is_first:
                if thebid.bid >= last_bid:
                    # listing.bid = thebid.bid
                    # listing.save()    --I handled this in the models.py using the @receiver. 
                    thebid.save()
                    request.user.watchlist.add(thebid.listing)
                    return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))
                else:

                    bidmessage ="Your bid should be bigger or equal to the starting bid"
                    commentform  = CommentForm()
                    bidform = BidForm()
                    listing_bid = float(listing.bid)


                    context = {'listing':listing,'bidform':bidform,'listing_bid':listing_bid,'commentform':commentform,'bidmessage':bidmessage}
                    return render(request,'auctions/listing.html',context)

            else:
                if thebid.bid > last_bid:
                    thebid.save()
                    request.user.watchlist.add(thebid.listing)
                    return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))
                else:
                    bidmessage ="Your bid should be bigger than  the current bid"
                    commentform  = CommentForm()
                    bidform = BidForm()
                    listing_bid = float(listing.bid)


                    context = {'listing':listing,'bidform':bidform,'listing_bid':listing_bid,'commentform':commentform,'bidmessage':bidmessage}
                    return render(request,'auctions/listing.html',context)


        else:
            print(bidform.errors)
            

    return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))








@login_required
def watchlist(request):
    return render(request,'auctions/watchlist.html')

@login_required
def addwatchlist(request,listing_id):
    listing = Listings.objects.get(id=listing_id)

    if listing not in request.user.watchlist.all():
        request.user.watchlist.add(listing)
        return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))
    else:
        return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))


@login_required
def removewatchlist(request,listing_id):
    listing = Listings.objects.get(id=listing_id)
    
    request.user.watchlist.remove(listing)
    return HttpResponseRedirect(reverse('auctions:watchlist'))


def categories(request):
    
    categories = Category.objects.all()
    context = {'categories':categories}
    return render(request,'auctions/categories.html',context)




def category(request,category_id):
    
    category = Category.objects.get(id=category_id)

    category_listings = Listings.objects.filter(category = category.name).filter(winner=None)

    

    context = {'category':category,'catList':category_listings}

    return render(request,'auctions/category.html',context)



@login_required
def comment(request,listing_id):
    listing = Listings.objects.get(id=listing_id)

    if request.method == 'POST':
        commentform = CommentForm(request.POST)

        if commentform.is_valid():
            thecomment = commentform.save(commit=False)
            thecomment.user = request.user
            thecomment.listing = listing
            thecomment.save()
            return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))
    
    return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))

    

@login_required
def closeauction(request,listing_id):
    listing = Listings.objects.get(id=listing_id)
    if request.user == listing.user:
        listing.winner = request.user
        listing.save()

        for bid in listing.bids.all():
            bid.user.watchlist.add(listing)

        
        return HttpResponseRedirect(reverse('auctions:listing',args=(listing.id,)))
    







