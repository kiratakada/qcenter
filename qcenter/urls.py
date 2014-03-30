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

    url(r'^%s/static/(?P<path>.*)$' % (settings.PROJECT_NAME), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
