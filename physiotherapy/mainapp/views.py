

# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment, ProgressReport
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
    appointments = Appointment.objects.all().order_by('date', 'time')
    return render(request, 'appointment_list.html', {'appointments': appointments})

# Progress Report View
def progress_report(request):
    reports = ProgressReport.objects.all()
    return render(request, 'progress_report.html', {'reports': reports})

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
