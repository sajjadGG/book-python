"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

from django.contrib import admin
from django.utils.translation import ugettext as _
from ..models.pings import *


class PingsAdmin ( admin.ModelAdmin ):
  list_select_related = True
  search_fields = ['host__ip', ]
  list_display = ( 'host', 'date' )
  list_display_links = ( 'host', )

admin.site.register( Ping, PingsAdmin )
