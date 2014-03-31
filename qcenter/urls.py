from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'data.views.user_login', name='user_login'),
    url(r'^%s/$' % (settings.PROJECT_NAME), 'data.views.user_login', name = 'user_login'),
    url(r'^%s/login/$' % (settings.PROJECT_NAME), 'data.views.user_login', name = 'user_login'),
    url(r'^%s/logout/$' % (settings.PROJECT_NAME), 'data.views.user_logout', name = 'user_logout'),

    url(r'^%s/register/$' % (settings.PROJECT_NAME), 'data.views.user_register', name = 'user_register'),

    url(r'^%s/dashboard/$' % (settings.PROJECT_NAME), 'data.views.dashboard', name = 'dashboard'),

    url(r'^%s/hospital/(?P<hos_id>\w+)/$' % (settings.PROJECT_NAME), 'data.views.hospital_details', name = 'hospital'),
    url(r'^%s/schedule/(?P<doc_id>\w+)/(?P<sch_id>\w+)/$' % (settings.PROJECT_NAME), 'data.views.doctor_schedule_details', name = 'doc_schedule'),
    url(r'^%s/form/$' % (settings.PROJECT_NAME), 'data.views.doctor_form', name = 'doctor_form'),

    url(r'^%s/static/(?P<path>.*)$' % (settings.PROJECT_NAME), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^%s/display/(?P<path>.*)$' % (settings.PROJECT_NAME), 'django.views.static.serve', {'document_root': settings.IMAGE_ROOT}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
