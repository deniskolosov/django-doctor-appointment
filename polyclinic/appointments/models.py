from django.db import models

# Create your models here.

class Doctor(models.Model):
    
    name = models.CharField(max_length = 100)
    specialization = models.CharField(max_length = 40)

    def __str__(self):
        return 'Врач {0}, {1}'.format(self.name, self.specialization)

class Appointment(models.Model):

    patient_name = models.CharField(max_length=40)
    patient_middlename = models.CharField(max_length=40)
    patient_surname = models.CharField(max_length=40)
    doctor = models.ForeignKey(Doctor)
    appointment_time = models.DateTimeField()

    def __str__(self):
        return '[{0} {1} {2} записан на прием у {3}, {4}'.format(self.patient_name, self.patient_middlename,
                self.patient_surname, self.doctor.name, self.doctor.specialization)
