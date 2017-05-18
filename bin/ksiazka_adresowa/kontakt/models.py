from django.db import models
from django.utils.translation import ugettext_lazy as _


class Adress(models.Model):
    contact = models.ForeignKey(verbose_name=_('Contact'), to='kontakt.contact')
    street = models.CharField(verbose_name=_('Street'), max_length=50)
    city = models.CharField(verbose_name=_('City'), max_length=50)

    def __str__(self):
        return f'{self.street} {self.city}'


class Contact(models.Model):
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50, db_index=True)
    phone = models.IntegerField(verbose_name=_('Phone'))
    date_of_birth = models.DateField(verbose_name=_('Date of Birth'), blank=True, null=True)
    photo = models.ImageField(verbose_name=_('Photo'), blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
