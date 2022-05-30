from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    customer = models.ForeignKey(verbose_name=_('Customer'), to='customer.Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(verbose_name=_('Product'), to='product.Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
