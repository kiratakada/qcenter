from django.db import models
from django.contrib.auth.models import User
from master.models import *


DAY_CHOICES = (
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday')
)

class Roles(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(null = True, blank = True)
    hospital = models.ForeignKey(Hospital)

    def __unicode__(self):
        return "%s" % self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)

    gender = models.IntegerField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)

    role = models.ForeignKey(Roles, null=True,  blank=True)
    country = models.ForeignKey(Country, null=True,  blank=True)
    city = models.ForeignKey(City, null=True,  blank=True)

    def __unicode__(self):
        return "%s" % self.user

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True,  blank=True)
    gender = models.IntegerField()
    hospital = models.ForeignKey(Hospital)
    specialist = models.ForeignKey(Specialist)
    is_active = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=50)
    patient_quota = models.IntegerField()

    def __unicode__(self):
        return "%s" % self.name

    def get_schedule(self):
        sch = DoctorSchedule.objects.filter(doctor=self.id)
        return sch

class DoctorSchedule(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    hospital = models.ForeignKey(Hospital)
    doctor = models.ForeignKey(Doctor)

    days = models.IntegerField()
    hours = models.CharField(max_length=50, null=True,  blank=True)
    patient_quota = models.IntegerField()

    def __unicode__(self):
        return "%s" % self.doctor.name


class SickReport(models.Model):
    subject = models.CharField(max_length=250, null=True, blank=True)
    medicine_report = models.CharField(max_length=250, null=True, blank=True)
    trauma = models.CharField(max_length=250, null=True, blank=True)
    date_from = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.subject


class Queue(models.Model):
    user = models.ForeignKey(User)
    schedule = models.ForeignKey(DoctorSchedule)
    date = models.DateTimeField()
    receipt_number = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField()
    sick_report = models.ForeignKey(SickReport, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.user

class HospitalNews(models.Model):
    news_title = models.CharField(max_length=100)
    news_content = models.TextField(null = True, blank = True)
    image = models.CharField(max_length=250, null=True, blank=True)
    is_active = models.BooleanField()

    def __unicode__(self):
        return "%s" % self.news_title
    