from django.contrib import admin

from master.models import *

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Hospital)
admin.site.register(CategorySpecialist)
admin.site.register(Specialist)