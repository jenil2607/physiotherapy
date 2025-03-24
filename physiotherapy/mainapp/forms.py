from django import forms
from .models import Appointment, Patient


class AppointmentForm(forms.ModelForm):
    patient_name = forms.CharField(
        max_length=100, 
        label="Patient Name", 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Patient Name'})
    )
    
    patient_age = forms.IntegerField(required=True, label="Patient Age")

    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_age', 'therapist', 'treatment', 'date', 'time']
        widgets = {
            'date': forms.TextInput(attrs={'class': 'datepicker', 'placeholder': 'Select Date'}),
            'time': forms.TextInput(attrs={'class': 'timepicker', 'placeholder': 'Select Time'}),
        }

    def save(self, commit=True):
        patient_name = self.cleaned_data.pop('patient_name')
        patient_age = self.cleaned_data.pop('patient_age')

        patient, created = Patient.objects.get_or_create(name=patient_name, defaults={'age': patient_age})
        self.instance.patient = patient  
        
        return super().save(commit)