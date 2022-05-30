from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    ean13 = models.CharField(verbose_name=_('Ean13'), max_length=13, null=False, blank=False, unique=True)
    name = models.CharField(verbose_name=_('Name'), max_length=13, null=False, blank=False, db_index=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=7, decimal_places=2, null=True, blank=True, default=None, help_text=_('Net price (without tax)'))

    def __str__(self):
        return f'{self.name} [{self.ean13}]'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
