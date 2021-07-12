from django.views.generic import TemplateView, DetailView, ListView
#from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Appointment

class AppointmentView(ListView):
    model = Appointment
    template_name = 'appointment.html'
    fields = ('Full_Name', 'schedule', 'doctor',)

class BookAppointmentView(CreateView):
    model = Appointment
    template_name = 'book_appointment.html'
    fields = ('Full_Name', 'schedule', 'doctor', 'date',)

class LookAppointmentView(ListView):
    model = Appointment
    template_name = 'look_appointment.html'
    fields = ('Full_Name', 'schedule', 'doctor',)
    
class AppointmentDetailView(DetailView): 
    model = Appointment
    template_name = 'appointment_detail.html'