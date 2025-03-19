from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy

# Home Page
def home(request):
    template = loader.get_template('home.html')  
    context = {'current_page': 'home'}
    return HttpResponse(template.render(context, request))


def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments,
        'current_page': 'appointments'  
    }
    template = loader.get_template('appointment_list.html')  
    return HttpResponse(template.render(context, request))

# Book Appointment View
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  
    else:
        form = AppointmentForm()
    
    template = loader.get_template('book_appointment.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

