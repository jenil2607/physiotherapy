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
    
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            print(f"Appointment saved: ID={appointment.id}, Patient={appointment.patient.name}, Date={appointment.date}, Time={appointment.time}")
            return redirect('appointment_list')  # Redirect to list view
        else:
            print("Form errors:", form.errors)  # Print validation errors
    else:
        form = AppointmentForm()
    
    template = loader.get_template('book_appointment.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))

def appointment_list(request):
    appointments = Appointment.objects.all()
    print(f"Retrieved {appointments.count()} appointments:", [str(apt) for apt in appointments])  # Debug output
    context = {
        'appointments': appointments,
        'current_page': 'appointments'
    }
    template = loader.get_template('appointment_list.html')
    return HttpResponse(template.render(context, request))

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('/')  # Redirect after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'signin.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/signin/')  # Redirect to signin after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})