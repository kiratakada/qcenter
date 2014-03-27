from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qcenter.views.home', name='home'),
    # url(r'^qcenter/', include('qcenter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^%s/static/(?P<path>.*)$' % (settings.PROJECT_NAME), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
