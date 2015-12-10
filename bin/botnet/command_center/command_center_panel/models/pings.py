"""
  Pawel Wylecial
  h0wl@cc-team.org

  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

import hosts
import datetime
from django.db import models
from django.utils.translation import ugettext as _


class Ping ( models.Model ):
    host = models.ForeignKey(hosts.Host, verbose_name=_('Host'), editable=True)
    date = models.DateTimeField ( verbose_name=_('Last seen'), auto_now_add=True, editable=True )

    def __unicode__( self ):
        return self.host

    class Meta ():
        ordering = ( 'date', )
        verbose_name = _( 'Ping' )
        verbose_name_plural = _( 'Pings' )
        app_label = 'command_center_panel'
