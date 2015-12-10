"""
  Pawel Wylecial
  h0wl@cc-team.org
  
  Matt Harasymczuk
  matt@harasymczuk.pl
  www.matt.harasymczuk.pl
"""

import datetime
from django.db import models
from django.utils.translation import ugettext as _


class Host ( models.Model ):
  ip = models.IPAddressField (verbose_name=_('IP Address'), unique=False)
  port = models.PositiveIntegerField ( verbose_name=_('Port') )#, max_value=65535 )
  active = models.BooleanField ( verbose_name=_('Is Host Active?'), default=True, blank=False, null=False )
  last_active = models.DateTimeField ( verbose_name=_('Last active'), auto_now=True )
  
  def __unicode__( self ):
    return '%s:%s' % ( self.ip, self.port )
  
  class Meta ():
    ordering = ( 'active', 'last_active' )
    verbose_name = _( 'Host' )
    verbose_name_plural = _( 'Hosts' )
    app_label = 'command_center_panel'
