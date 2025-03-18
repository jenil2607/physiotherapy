from django.contrib import admin

# Register your models here.
from .models import Patient, Therapist, Treatment, Appointment

admin.site.register(Patient)
admin.site.register(Therapist)
admin.site.register(Treatment)
admin.site.register(Appointment)

