from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'users/home.html')

    return HttpResponseRedirect(reverse("users:login"))


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:home"))
        else:
            context = {'message': 'Invalid data','notflightpage':True}
            return render(request, 'users/login.html', context)

    return render(request, 'users/login.html',{'notflightpage':True})


@login_required
def logout_page(request):
    logout(request)
    return render(request, 'users/login.html', {'message': 'Logged Out', 'logout': 'true','notflightpage':True})


def register(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
    #   birthdate = request.POST['birthdate']
    #   gender = request.POST['gender']


        for person in User.objects.values('username','email'):
            if (person['username'],person['email']) == (username,email) :
                return render(request,'users/register.html',{'exist': 'TrueTrue'})
                break
            elif person['username'] == username and person['email'] != email:
                return render(request,'users/register.html',{'exist': 'TrueFalse'})
                break
            elif person['email'] == email and person['username'] != username:
                return render(request,'users/register.html',{'exist': 'FalseTrue','notflightpage':True})
                break


            
        user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
        user.save()
        login(request, user)

        return HttpResponseRedirect(reverse("users:home"))

    return render(request, 'users/register.html',{'notflightpage':True})
