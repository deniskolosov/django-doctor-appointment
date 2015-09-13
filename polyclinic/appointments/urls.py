from django.conf.urls import url


from . import views

urlpatterns = [
        url(r'^$', views.AppointmentCreateView.as_view(),
            name='form'),
        ]
