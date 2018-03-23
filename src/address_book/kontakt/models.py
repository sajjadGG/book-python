from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    kontakt = models.ForeignKey(verbose_name=_('Kontakt'), to='kontakt.Kontakt', on_delete=models.CASCADE)
    street = models.CharField(verbose_name=_('Street'), max_length=30)
    city = models.CharField(verbose_name=_('City'), max_length=30)

    def __str__(self):
        return f'{self.kontakt} zamieszkały {self.street}, {self.city}'


class Kontakt(models.Model):
    created = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    modified = models.DateTimeField(verbose_name=_('Modifed'), auto_now=True)
    first_name = models.CharField(verbose_name=_('First Name'), max_length=30)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=30)
    date_of_birth = models.DateField(verbose_name=_('Date of birth'))
    image = models.ImageField(verbose_name=_('Image'), blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('Kontakt')
        verbose_name_plural = _('Kontakty')