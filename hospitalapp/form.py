from hospitalapp.models import Booking
from django import forms

class bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
