from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iamriel.views.home', name='home'),
    # url(r'^iamriel/', include('iamriel.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
