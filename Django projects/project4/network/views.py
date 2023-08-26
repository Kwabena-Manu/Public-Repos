from asyncio.windows_events import NULL
from telnetlib import STATUS
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import json


from .models import User,Post


def index(request):
    posts = Post.objects.all();
    # Return Posts in chronological order
    posts = posts.order_by("-timestamp").all()
    
    paginator = Paginator(posts,per_page=10)
    
    if len(posts)!= 0:
        if request.GET.get('page') == None :
            page = 1
        else:
            page = int(request.GET.get('page'))
        posts = paginator.page(page)
        print("My posts",posts[0].content)
        context = {"empty":False,"posts": posts}   
        return render(request, "network/index.html", context)
    else:
        
        context={'empty': True}
        return render(request, "network/index.html", context)



def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def addPost(request):
    if request.method != "POST":
        return JsonResponse({
            "error": "POST request required"
        }, status=400)
        
    data = json.loads(request.body)
    print("The data is ",data)
    
    postcontent = data.get("post")
    
    if postcontent is not NULL:
        post = Post(
            content= postcontent,
            owner = request.user,
        )
        
        post.save()
        
    return JsonResponse({"message": "Post sent successfully."}, status=201)


@csrf_exempt
@login_required
def editPost(request,postID):
    if request.method != "POST":
        return JsonResponse({
            "error": "POST request required"
        }, status=400)
        
    data = json.loads(request.body)
    print("The data is ",data)
    
    postcontent = data.get("post")
    
    if postcontent is not NULL:
        originalPost = Post.objects.get(id=postID)
        if originalPost :
            originalPost.content = postcontent
       
    
        
        originalPost.save()
        
    return JsonResponse({"message": "Post sent successfully."}, status=201)
    
    
    
@csrf_exempt 
def loadPosts(request):
    
    posts = Post.objects.all()
    
    # Return Posts in chronological order
    posts = posts.order_by("-timestamp").all()
    return JsonResponse([post.serialize() for post in posts],safe= False)

@csrf_exempt 
@login_required
def likePost(request,postID):
    if request.method != "POST":
        return JsonResponse({
            "error": "POST request required"
        }, status=400)
    post = Post.objects.get(id=postID)
    
    if post:    
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return JsonResponse({"message": "User successfully unliked post."}, status=201)
            
        else:
            post.likes.add(request.user)
            return JsonResponse({"message": "User successfully liked post."}, status=201)
    else:
            return JsonResponse({"message": "Post doesn't exit"}, status=500    )
        
        


@login_required
def following(request):
      userlist = [user for user in  User.objects.get(username=request.user).following.all()]
      print("userlist contains", userlist)
      filteredPosts = []
      
      for post in Post.objects.all().order_by('-timestamp'):
        if post.owner in userlist:
            filteredPosts.append(post)
      
      paginator = Paginator(filteredPosts,per_page=10)
    
      if len(filteredPosts)!= 0:
          if request.GET.get('page') == None :
              page = 1
          else:
              page = int(request.GET.get('page'))
          posts = paginator.page(page)
          context = {"empty":False,"posts": posts}   
          return render(request, "network/following.html", context)
      else:
          
          context={'empty': True}
          return render(request, "network/following.html", context)

            

@login_required
def profile(request):
    theuser = User.objects.get(username=request.user)
    posts=[]
    for post in Post.objects.all().order_by("-timestamp"):
        if post.owner == theuser:
            posts.append(post)
    
    paginator = Paginator(posts,per_page=10)
    
    if len(posts)!= 0:
         if request.GET.get('page') == None :
             page = 1
         else:
             page = int(request.GET.get('page'))
         posts = paginator.page(page)
         context = {"empty":False,"account":theuser,"posts":posts}   
         return render(request, "network/profile.html", context)
    else:
          
         context={'empty': True}
         return render(request, "network/profile.html", context)

   
   
    
@login_required
def notprofile(request,userid):
    theuser = User.objects.get(id=userid)
    posts=[]
    for post in Post.objects.all().order_by("-timestamp"):
        if post.owner == theuser:
            posts.append(post)
    
    paginator = Paginator(posts,per_page=10)
    
    if len(posts)!= 0:
         if request.GET.get('page') == None :
             page = 1
         else:
             page = int(request.GET.get('page'))
         posts = paginator.page(page)
         context = {"empty":False,"account":theuser,"posts":posts}   
         return render(request, "network/profile.html", context)
    else:
          
         context={'empty': True}
         return render(request, "network/profile.html", context)
     
     
@csrf_exempt
@login_required    
def follow(request,userid):
    if request.method != "POST":
        return JsonResponse({
            "error": "POST request required"
        }, status=400)
        
    requestUser = User.objects.get(username=request.user)
    accountOwner = User.objects.get(id=userid)
    
    if accountOwner not in requestUser.following.all():
        requestUser.following.add(accountOwner)
        return JsonResponse({"message": "Successfully added to following","status":1}, status=201)
    else:
        requestUser.following.remove(accountOwner)
        return JsonResponse({"message": "Successfully removed to following","status":0}, status=201)
        
    
    