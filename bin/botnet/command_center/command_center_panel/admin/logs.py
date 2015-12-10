"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

from django.contrib import admin
from django.utils.translation import ugettext as _
from ..models.logs import *


class LogsAdmin ( admin.ModelAdmin ):
  list_select_related = True
  search_fields = ['host__ip', ]
  list_display = ( 'host', 'date', 'log' )
  list_display_links = ( 'host', )

admin.site.register( Log, LogsAdmin )
