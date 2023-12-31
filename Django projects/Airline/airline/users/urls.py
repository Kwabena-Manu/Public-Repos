from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.login_page,name="login"),
    path("logout/",views.logout_page,name="logout"),
    path("home", views.home,name="home"),
    path("register/",views.register, name="register")
]
