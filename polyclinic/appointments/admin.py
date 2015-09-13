from django.contrib import admin

from .models import Doctor, Appointment


class AppointmentAdmin(admin.ModelAdmin):
    fields = [
            'patient_name',
            'patient_middlename',
            'patient_surname',
            'doctor',
            'appointment_time'
            ]

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization',
            'appointments_month')


            
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment, AppointmentAdmin)

# Register your models here.

