from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Patient Model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Therapist Model
class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    experience = models.IntegerField()  # Number of years
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Treatment Model
class Treatment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.name

# Appointment Model

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    therapist_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient_name} - {self.date} {self.time}"

# Progress Report Model
class ProgressReport(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    notes = models.TextField()
    progress_percentage = models.IntegerField(help_text="Progress in percentage")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress for {self.appointment.patient.name} - {self.progress_percentage}%"
