from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib import messages

from datetimewidget.widgets import DateTimeWidget

from .models import Appointment


class AppointmentCreateMixin(object):

    fields = ('patient_name',
              'patient_middlename',
              'patient_surname',
              'doctor',
              'appointment_time')

    @property
    def success_msg(self):
        return NonImplemented

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super(AppointmentCreateMixin, self).form_valid(form)

class AppointmentCreateView(AppointmentCreateMixin, CreateView):
    model = Appointment
    fields = ('patient_name',
              'patient_middlename',
              'patient_surname',
              'doctor',
              'appointment_time')
    success_msg = "Спасибо! Вы записались на прием."

    def get_form(self, form_class):
        form = super(AppointmentCreateView, self).get_form()
        dateTimeOptions = {
            'weekStart': '1',
            'format': 'dd/mm/yyyy HH',
            'daysOfWeekDisabled': "'0,6'",
            'minuteStep': '60',
        }
        form.fields['appointment_time'].widget = DateTimeWidget(
            options=dateTimeOptions, usel10n=True, bootstrap_version=3)

        return form

    def form_valid(self, form):
        import datetime
        start_date = form.cleaned_data['appointment_time']
        end_date = form.cleaned_data['appointment_time'] + \
            datetime.timedelta(hours=1)

        if not datetime.time(9, 00) \
                <= start_date.time() < datetime.time(18, 00):
            form.add_error('appointment_time', 'Часы приема — 09:00-18:00')
            return self.form_invalid(form)
        if start_date.weekday() == 5 or start_date.weekday() == 6:
            form.add_error('appointment_time', 'Дни приема — ПН-ПТ')
            return self.form_invalid(form)

        if Appointment.objects.filter(appointment_time__range=(start_date,
                                                               end_date)):
            form.add_error('appointment_time', 'К сожалению, время занято!')
            return self.form_invalid(form)
        return super(AppointmentCreateView, self).form_valid(form)

    template_name = 'appointments/appointment_form.html'
