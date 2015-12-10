from django.db import models
from django.utils.translation import ugettext_lazy as _


class Address(models.Model):
    contact = models.ForeignKey(verbose_name=_('Address'), to='contact.Contact')
    street = models.CharField(verbose_name=_('Street'), max_length=50)
    city = models.CharField(verbose_name=_('City'), max_length=50)
    zip_code = models.CharField(verbose_name=_('Zip Code'), max_length=10)
    country = models.CharField(verbose_name=_('Country'), max_length=40)

    def __str__(self):
        return '{street}, {zip_code} {city}, {country}'.format(**self.__dict__)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Adresses')
        ordering = ['country', '-city']


class Document(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')
        ordering = ['name']


class Contact(models.Model):
    GENDER_CHOICES = [
        ('male', _('Male')),
        ('female', _('Female'))
    ]

    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50, db_index=True)
    phone = models.IntegerField(verbose_name=_('Phone'), null=True, blank=True)
    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)
    gender = models.CharField(verbose_name=_('Gender'), max_length=10, null=True, choices=GENDER_CHOICES, db_index=True)
    document_type = models.ForeignKey(verbose_name=_('Document Type'), to='contact.Document', )
    document_number = models.CharField(verbose_name=_('Document Number'), max_length=15, null=True, blank=True)
    photo = models.FileField(verbose_name=_('Photo'), null=True)

    def __str__(self):
        return "{last_name} {first_name}".format(**self.__dict__)

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ['last_name', 'first_name']