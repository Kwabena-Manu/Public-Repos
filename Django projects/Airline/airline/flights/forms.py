from django import forms
from .models import Passenger


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields =['user','flights']
        labels ={'user':'User','flights': 'FLIGHT'}
