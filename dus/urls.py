from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # TEMPORARY DESING TEMPLATES ------------------------
    url('^$', direct_to_template, {'template': 'design/index.html'}, name='index'),
    url('^analyse/$', direct_to_template, {'template': 'design/analytics/index.html'}, name='index'),
    url('^analyse/link$', direct_to_template, {'template': 'design/analytics/link.html'}, name='index'),
    # END: TEMPORARY DESING TEMPLATES -------------------
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^uploads/(?P<path>.*)$', 'serve'),
    )

