from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)

    def __unicode__(self):
        return "%s" % self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return "%s" % self.name

    def get_hospital(self):
        hospital = Hospital.objects.filter(city=self.id)
        return hospital


class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(null = True, blank = True)
    phone = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    city = models.ForeignKey(City)

    def __unicode__(self):
        return "%s" % self.name

    def get_specialist(self):
        doctors = Doctor.objects.filter(hospital=self.id)
        return doctors


class CategorySpecialist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)

    def __unicode__(self):
        return "%s" % self.name

class Specialist(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    category = models.ForeignKey(CategorySpecialist)

    def __unicode__(self):
        return "%s" % self.name










