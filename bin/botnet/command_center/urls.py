"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""


from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^command_center/', include('command_center.foo.urls')),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^', include(admin.site.urls)),
)
