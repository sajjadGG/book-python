from django.db import models
from django.utils.translation import gettext_lazy as _


class AddressType(models.TextChoices):
    BILLING = 'billing', _('Billing')
    SHIPPING = 'shipping', _('Shipping')


class Address(models.Model):
    customer = models.ForeignKey(verbose_name=_('Customer'), to='customer.Customer', on_delete=models.CASCADE)
    type = models.CharField(verbose_name=_('Type'), max_length=50, null=True, blank=True, default=None, choices=AddressType.choices)
    street = models.CharField(verbose_name=_('Street'), max_length=70, null=True, blank=True, default=None)
    postcode = models.CharField(verbose_name=_('Post Code'), max_length=50, null=True, blank=True, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=True, blank=True, default=None)
    region = models.CharField(verbose_name=_('Region'), max_length=50, null=True, blank=True, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=50, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'{self.customer} {self.type}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Customer(models.Model):
    firstname = models.CharField(verbose_name=_('First Name'), max_length=50)
    lastname = models.CharField(verbose_name=_('Last Name'), max_length=50, db_index=True)
    born = models.DateField(verbose_name=_('Birthday'), null=True, blank=True, default=None)
    gender = models.CharField(verbose_name=_('Gender'), max_length=20, null=True, blank=True, default=None)
    email = models.EmailField(verbose_name=_('Email'), max_length=100, null=True, blank=True, default=None, unique=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=20, null=True, blank=True, default=None)
    tax_number = models.CharField(verbose_name=_('Tax Number'), max_length=20, null=True, blank=True, default=None)

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
