from django.shortcuts import render,redirect
from .models import Flight,Passenger
from .forms import PassengerForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.



def homepage(request):
    return render(request,'flights/homepage.html')

@login_required
def index(request):
    context ={'flights': Flight.objects.all()}

    return render(request,"flights/index.html",context)

@login_required
def flight(request,flight_id):
    theflight = Flight.objects.get(pk=flight_id) #pk same as id
    itspassengers = theflight.passengers.all()
    
    non_passengers = Passenger.objects.exclude(flights=theflight).all()
    context = {'flight': theflight,'passengers': itspassengers,'non_passengers':non_passengers}

    return render(request,'flights/flight.html',context)

@login_required
def book(request,flight_id):
    checker = request.POST.get("code1")
    if checker == "true":
        if request.method == 'POST':
            theflight = Flight.objects.get(id=flight_id)

            passenger = Passenger.objects.get(id=int(request.POST["passenger"]))
            passenger.flights.add(theflight)
            return HttpResponseRedirect(reverse('flights:flight',args=(theflight.id,)))


# My Code
    # else:
    #     theflight = Flight.objects.get(pk =flight_id)

    #     if request.method != 'POST':
    #         form = PassengerForm()
    #     else:
    #         form = PassengerForm(data=request.POST)

    #         if form.is_valid:
    #             form.save()
    #             return redirect('flights:index')

    #     allFlights = Flight.objects.all()
    #     context={'form': form, 'flight':theflight, 'allflights': allFlights}

    #     return render(request,'flights/book.html',context)
        
   
# My Code 2
    else:
        flight = Flight.objects.get(id=flight_id)



        exist=False
        allFlights = Flight.objects.all()
        passenger = request.user.passenger
        if request.method == 'POST':
            theflight = Flight.objects.get(id=int(request.POST['flights']))
            non_passengers = Passenger.objects.exclude(flights=theflight).all()
            flightpass = theflight.passengers.all()
            passflights = passenger.flights.all()



        
            if theflight in passflights:
                exist = True
            else:
                passenger.flights.add(theflight)
            
            return render(request,'flights/flight.html',{'flight':theflight,'non_passengers':non_passengers,'passengers':flightpass})
            
            
    
    
        context = {'flight':flight,'exist':exist}

        return render(request,'flights/book.html',context)



def myflights(request):

    flights = request.user.passenger.flights.all()
    myflightpage = True
    return render(request,"flights/myflights.html",{'flights':flights,'myflightpage':myflightpage})



def removeflight(request,flight_id):
    theflight = Flight.objects.get(id=flight_id)

    request.user.passenger.flights.remove(theflight)

    flights = request.user.passenger.flights.all()

    return render(request,'flights/myflights.html',{'flights':flights})


