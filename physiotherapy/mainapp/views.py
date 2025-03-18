from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Home Page
def home(request):
    return render(request, 'home.html')

# Appointment Booking View
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  
    else:
        form = AppointmentForm()
    
    return render(request, 'book_appointment.html', {'form': form})

# Appointment List View
def appointment_list(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments,
        'current_page': 'appointments'  
    }
    template = loader.get_template('appointment_list.html')  
    return HttpResponse(template.render(context, request))


# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

# Signup View
def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
