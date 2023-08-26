from operator import truediv
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    following = models.ManyToManyField("User",symmetrical=False,related_name="followers")
    
class Post(models.Model):
    content = models.TextField(blank=True)
    owner = models.ForeignKey("User", on_delete=models.CASCADE, blank=False, null=False)
    likes = models.ManyToManyField("User", related_name="posts_liked",blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    
    def serialize(self):
            return {
                "id": self.id,
                "content": self.content,
                "owner": self.owner.username,
                "likes": [user.username for user in self.likes.all()],
                "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p")
            }