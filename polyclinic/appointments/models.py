import datetime
from django.db import models

# Create your models here.

class Doctor(models.Model):
    
    name = models.CharField(max_length = 100)
    specialization = models.CharField(max_length = 40)

    def __str__(self):
        return 'Врач {0}, {1}'.format(self.name, self.specialization)

    def appointments_month(self):
        today = datetime.datetime.today()
        return Appointment.objects.filter(
                appointment_time__year=today.year,
                appointment_time__month=today.month
                )


class Appointment(models.Model):

    patient_name = models.CharField('Ваше имя:', max_length=40)
    patient_middlename = models.CharField('Ваше отчество:', max_length=40)
    patient_surname = models.CharField('Ваша фамилия:', max_length=40)
    doctor = models.ForeignKey(Doctor, verbose_name="Выберите врача:")
    appointment_time = models.DateTimeField('Дата записи:')

    def __str__(self):
        return '[{0} {1} {2} записан на прием у {3}, {4} на {5}'.format(
                self.patient_name,
                self.patient_middlename,
                self.patient_surname,
                self.doctor.name,
                self.doctor.specialization,
                self.appointment_time)

    def get_absolute_url(self):
            return "/"


