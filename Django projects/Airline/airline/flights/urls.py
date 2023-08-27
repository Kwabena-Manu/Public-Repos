from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("index",views.index,name="index"),
    path("<int:flight_id>/", views.flight, name="flight"),
    path("<int:flight_id>/book/", views.book, name="book"),
    path("myflights/",views.myflights,name="myflights"),
    path("myflights/removeflight/<int:flight_id>",views.removeflight,name="removeflight")
    
]
