from django import forms
from .models import Appointment, Patient, Review, TherapySession
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AppointmentForm(forms.ModelForm):
    
    patient_name = forms.CharField(
        max_length=100, 
        label="Patient Name", 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Patient Name'})
    )
    patient_age = forms.IntegerField(required=True, label="Patient Age")
    patient_contact = forms.CharField(
        max_length=15,
        label="Patient Contact",
        widget=forms.TextInput(attrs={'placeholder': 'Enter Contact'})
    )

    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_age', 'patient_contact', 'therapist', 'treatment', 'date', 'time']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'Select Date'}),
            'time': forms.TextInput(attrs={'class': 'timepicker', 'placeholder': 'Select Time'}),
        }

    def save(self, commit=True):
        patient_name = self.cleaned_data.pop('patient_name')
        patient_age = self.cleaned_data.pop('patient_age')
        patient_contact = self.cleaned_data.pop('patient_contact')

        patient, created = Patient.objects.get_or_create(
            name=patient_name,
            defaults={'age': patient_age, 'contact': patient_contact, 'medical_history': ''}  # Default for medical_history
        )
        print(f"Patient {'created' if created else 'retrieved'}: {patient.name}, ID={patient.id}")  # Debug
        self.instance.patient = patient
        
        # Ensure all required Appointment fields are set
        if not self.instance.therapist:
            raise ValueError("Therapist is required")
        if not self.instance.treatment:
            raise ValueError("Treatment is required")
        
        return super().save(commit)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']


class TherapySessionForm(forms.ModelForm):
    class Meta:
        model = TherapySession
        fields = ['title', 'description', 'date', 'time']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'Select Date'}),
            'time': forms.TextInput(attrs={'class': 'timepicker', 'placeholder': 'Select Time'}),
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']