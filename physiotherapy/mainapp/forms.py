from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'therapist', 'treatment', 'date', 'time']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'Select Date'}),
            'time': forms.TextInput(attrs={'class': 'timepicker', 'placeholder': 'Select Time'}),
        }
    

