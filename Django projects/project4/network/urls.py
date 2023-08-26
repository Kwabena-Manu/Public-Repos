
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile",views.profile,name="profile"),
    path("profile/<int:userid>",views.notprofile,name="notprofile"),
    path("following",views.following, name="following"),
    path("addpost", views.addPost, name="addpost"),
    path("editpost/<int:postID>", views.editPost, name="editpost"),
    path("likepost/<int:postID>",views.likePost,name="likepost"),
    path("loadposts",views.loadPosts, name="loadposts"),
    path("follow/<int:userid>", views.follow, name="follow")
]
