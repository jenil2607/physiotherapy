from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import timedelta


# Patient Model
class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    contact = models.CharField(max_length=15)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Therapist Model
class Therapist(models.Model):
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
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.patient.name} - {self.date} {self.time} ({self.status})"

class TherapySession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, null=True)
    therapist = models.ForeignKey('Therapist', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField(default=timedelta(minutes=30))  # Example default
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date} {self.time}"