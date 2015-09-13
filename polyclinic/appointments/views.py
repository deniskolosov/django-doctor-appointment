from django.shortcuts import render

from django.views.generic import CreateView

# Create your views here.


from .models import Appointment


class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ('patient_name',
            'patient_middlename',
            'patient_surname',
            'doctor',
            'appointment_time')

    template_name = 'appointments/appointment_form.html'

