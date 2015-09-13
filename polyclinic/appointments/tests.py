import datetime
from django.test import TestCase

# Create your tests here.
from .models import Appointment, Doctor

class AppointmentTest(TestCase):
    patient_name = "Иван"
    patient_surname = "Петров"
    patient_middlename = "Иванович"
    doctor = Doctor.objects.get(id=1)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)

    def create_appointment(
            self,
            patient_name,
            patient_middlename,
            patient_surname,
            doctor,
            tomorrow):
        return Appointment.objects.create(
                patient_name=patient_name,
                patient_middlename=patient_middlename,
                patient_surname=patient_surname,
                doctor=doctor,
                appointment_time=tomorrow)

    def test_appointment_creation(self):
        a = self.create_appointment(
                self.patient_name,
                self.patient_middlename,
                self.patient_surname,
                self.doctor,
                self.tomorrow)
        self.assertTrue(isinstance(a,Appointment))
