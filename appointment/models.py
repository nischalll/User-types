from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth import get_user_model


class Schedule(models.Model):
    schedule = models.CharField(max_length=30)

    def __str__(self):
        return self.schedule


class Doctor(models.Model):
    doctor = models.CharField(max_length=30)
   
    def __str__(self):
        return self.doctor




class Appointment(models.Model):
    Full_Name = models.CharField(max_length=255)
    schedule = models.ForeignKey(Schedule, on_delete=CASCADE)
    date = models.DateField()
    doctor = models.ForeignKey(Doctor, on_delete=CASCADE)
    #speciality = models.ForeignKey(Speciality, on_delete=CASCADE)


    def __str__(self):
        return self.Full_Name

    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])
