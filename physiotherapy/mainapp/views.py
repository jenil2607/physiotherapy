from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment, Review, TherapySession
from .forms import AppointmentForm, ReviewForm, TherapySessionForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

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


@login_required
def review_page(request):
    reviews = Review.objects.all()
    print(f"Retrieved {reviews.count()} reviews:", [str(review) for review in reviews])  # Debug output

    context = {
        'reviews': reviews,
        'current_page': 'reviews',
    }

    template = loader.get_template('review.html')  # Load the template
    return HttpResponse(template.render(context, request))  # Render and return response

def therapy_session_list(request):
    sessions = TherapySession.objects.all()
    return render(request, 'therapy_session.html', {'sessions': sessions})

def create_therapy_session(request):
    if request.method == "POST":
        form = TherapySessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('therapy_session_list')
    else:
        form = TherapySessionForm()
    
    return render(request, 'create_therapy_session.html', {'form': form})