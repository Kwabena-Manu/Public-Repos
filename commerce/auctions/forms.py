from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User,Listings,Bids,Comment


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email')
    
        
        


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username','email')


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listings
        exclude = ['user','winner']
        labels = {'title':'Title','bid':'Bid','description':'Description','category':'Category','listing_pic':'Image'}
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':''}),
            'bid': forms.NumberInput(attrs={'placeholder':''}),
            'description': forms.TextInput(attrs={'placeholder':''}),
            'category' : forms.TextInput(attrs={'placeholder':''}),
            'listing_pic' : forms.ClearableFileInput()
        }


class BidForm(forms.ModelForm):

    class Meta:
        model = Bids
        exclude = ['user','listing']
        labels = {'bid':''}
        widgets= {
            'bid' : forms.NumberInput(attrs={'step': 1,'placeholder':'Bid'})
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','listing','date_added']
        fields = ['comment']
        labels = {'comment':''}
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Leave a comment here'})
        }


        
