from django.urls import path
from .views import AppointmentView,LookAppointmentView,BookAppointmentView, AppointmentDetailView

urlpatterns = [
     path('<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('', AppointmentView.as_view(), name='appointment'),
    path('look/', LookAppointmentView.as_view(), name='look_appointment'),
    path('book/', BookAppointmentView.as_view(), name='book_appointment'),
]
