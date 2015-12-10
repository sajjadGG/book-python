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


class Log ( models.Model ):
  host = models.ForeignKey(hosts.Host, verbose_name=_('Host'), editable=True)
  date = models.DateTimeField ( verbose_name=_('Last seen'), auto_now_add=True, editable=True )
  log = models.TextField(verbose_name=_('Log'), blank=True, null=True, )

  def __unicode__( self ):
    return "%s %s" % (self.host, self.date)

  class Meta ():
    ordering = ( 'date', )
    verbose_name = _( 'Log' )
    verbose_name_plural = _( 'Logs' )
    app_label = 'command_center_panel'
