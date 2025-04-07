from django.http import HttpResponse
from django.template import loader

# Create your views here.
from django.shortcuts import render, redirect
from .models import Appointment, TherapySession
from .forms import AppointmentForm, TherapySessionForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
# admin login

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView






# Home Page
def home(request):
    template = loader.get_template('home.html')  
    context = {'current_page': 'home'}
    return HttpResponse(template.render(context, request))
    

@login_required
def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            appointment.user = request.user  # Set the user who booked the appointment
            appointment.save()
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
    appointments = Appointment.objects.filter(user=request.user)
    print(f"Retrieved {appointments.count()} appointments:", [str(apt) for apt in appointments])  # Debug output
    context = {
        'appointments': appointments,
        'current_page': 'appointments'
    }
    template = loader.get_template('appointment_list.html')
    return HttpResponse(template.render(context, request))


@method_decorator(staff_member_required, name='dispatch')
class Admin_Dashboard(TemplateView):
    template_name = 'admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.all()
        context['therapy_sessions'] = TherapySession.objects.all()
        return context


@login_required
def create_therapy_session(request):
    if request.method == "POST":
        form = TherapySessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('therapy_session_list')
    else:
        form = TherapySessionForm()
    return render(request, 'create_therapy_session.html', {'form': form})



@login_required
def therapy_session_list(request):
    sessions = TherapySession.objects.all()
    return render(request, 'therapy_session_list.html', {'sessions': sessions})