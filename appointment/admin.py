from django.contrib import admin
from .models import Schedule, Doctor, Appointment

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Doctor)
admin.site.register(Appointment)
