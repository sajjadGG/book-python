"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

from django.contrib import admin
from django.utils.translation import ugettext as _
from ..models.hosts import *


class HostsAdmin ( admin.ModelAdmin ):
  list_select_related = True
  search_fields = ['ip', ]
  list_display = ( 'ip', 'port', 'active', 'last_active' )
  list_display_links = ( 'ip', )

admin.site.register( Host, HostsAdmin )
