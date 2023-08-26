from django.contrib import admin
from .forms import UserCreationForm,UserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display =['id','username','email']

class BidsAdmin(admin.ModelAdmin):
    list_display=['id','user','listing','bid']


class CommentAdmin(admin.ModelAdmin):
    list_display=['id','user','listing','date_added']

admin.site.register(User,UserAdmin)
admin.site.register(Listings)
admin.site.register(Category)
admin.site.register(Bids,BidsAdmin)
admin.site.register(Comment,CommentAdmin)
