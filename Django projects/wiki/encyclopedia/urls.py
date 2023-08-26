from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random",views.randompage,name="randompage"),
    path("wiki/createpage",views.createentry,name="createentry"),
    path("wiki/<str:title>",views.entrypage,name="entrypage"),
    path("wiki/search/",views.search,name="search"),
    path("wiki/entry/editpage/<str:title>",views.editpage,name="editpage"),   
]
