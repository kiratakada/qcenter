from django.contrib import admin

from data.models import *

admin.site.register(Doctor)
admin.site.register(UserProfile)
admin.site.register(Roles)
admin.site.register(DoctorSchedule)
admin.site.register(SickReport)
admin.site.register(Queue)
admin.site.register(HospitalNews)