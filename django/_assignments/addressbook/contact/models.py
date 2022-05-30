from pathlib import Path
from datetime import date
from uuid import uuid4
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class BaseModel(models.Model):
    class Meta:
        abstract = True


class Rank(models.TextChoices):
    NORMAL = 'normal', _('Normal')
    SENIOR = 'senior', _('Senior')


class PhoneCountryCodes(models.TextChoices):
    POLAND = '+48', _('Poland')
    USA = '+1', _('USA')


class Type(models.TextChoices):
    UNSPECIFIED = None, _('Unknown')
    HOME = 'home', _('Home')
    WORK = 'work', _('Work')


class Nationality(models.TextChoices):
    POLAND = 'poland', _('Poland')
    USA = 'usa', _('USA')


class Phone(BaseModel):
    person = models.ForeignKey(verbose_name=_('Person'), to='contact.person', blank=False, null=None, default=None, on_delete=models.CASCADE)
    type = models.CharField(verbose_name=_('Type'), max_length=15, choices=Type.choices, blank=True, null=True, default=Type.UNSPECIFIED)
    country_code = models.CharField(verbose_name=_('Country Code'), max_length=10, choices=PhoneCountryCodes.choices, blank=False, null=True, default=None)
    number = models.CharField(verbose_name=_('Phone Number'), max_length=15, blank=False, null=True, default=None)

    class Meta:
        default_related_name = 'contact_phone'
        app_label = 'contact'
        verbose_name = _('Phone')
        verbose_name_plural = _('Phones')

    def __str__(self):
        return f'{self.country_code} {self.number}'


class Address(BaseModel):
    person = models.ForeignKey(verbose_name=_('Person'), to='contact.person', blank=False, null=None, default=None, on_delete=models.CASCADE)
    street = models.CharField(verbose_name=_('Street'), max_length=30, blank=False, null=False, default=None)
    house_number = models.CharField(verbose_name=_('House Number'), max_length=30, blank=False, null=False, default=None)
    apartment = models.CharField(verbose_name=_('Apartment'), max_length=30, blank=False, null=False, default=None)
    city = models.CharField(verbose_name=_('City'), max_length=30, blank=False, null=False, default=None)
    region = models.CharField(verbose_name=_('Region'), max_length=30, blank=False, null=False, default=None, help_text=_('State, Voivodeship, Canton, Land, Okres'))
    post_code = models.CharField(verbose_name=_('Post Code'), max_length=30, blank=False, null=False, default=None)
    country = models.CharField(verbose_name=_('Country'), max_length=30, blank=False, null=False, default=None)

    class Meta:
        default_related_name = 'contact_address'
        app_label = 'contact'
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f'{self.contact}'


def upload_to(filename) -> Path:
    filename = Path(filename).with_stem(uuid4().hex)
    return settings.MEDIA_ROOT / filename


class Person(BaseModel):
    ## System Fields
    add_date = models.DateTimeField(verbose_name=_('Add Date'), auto_now_add=True, editable=False, blank=True, null=True)
    add_author = models.ForeignKey(verbose_name=_('Add Author'), related_name='add_date', to='auth.User', blank=True, null=True, default=None, editable=False, on_delete=models.SET_NULL)
    edit_date = models.DateTimeField(verbose_name=_('Edit Date'), auto_now=True, editable=False, blank=True, null=True)
    edit_author = models.ForeignKey(verbose_name=_('Edit Author'), related_name='edit_date', to='auth.User', blank=True, null=True, default=None, editable=False, on_delete=models.SET_NULL)

    ## Personal Data
    firstname = models.CharField(verbose_name=_('First Name'), max_length=30, blank=False, null=False)
    lastname = models.CharField(verbose_name=_('Last Name'), max_length=30, blank=False, null=False, db_index=True)
    nationality = models.CharField(verbose_name=_('Nationality'), max_length=30, choices=Nationality.choices, blank=True, null=True, default=None)
    national_identification_number = models.CharField(verbose_name=_('National Identification Number'), max_length=20, blank=True, null=True, default=None)

    ## Biometric data
    birthday = models.DateField(verbose_name=_('Birthday'), blank=True, null=True, default=None)
    height = models.FloatField(verbose_name=_('Height'), blank=True, null=True, default=None, validators=[MinValueValidator(150), MaxValueValidator(210)], help_text=_('cm'))
    weight = models.FloatField(verbose_name=_('Weight'), blank=True, null=True, default=None, validators=[MinValueValidator(50), MaxValueValidator(90)], help_text=_('kg'))
    image = models.ImageField(verbose_name=_('Image'), upload_to=upload_to, blank=True, null=True, default=None)

    ## Professional
    is_astronaut = models.BooleanField(verbose_name=_('Is Astronaut?'), blank=True, null=True, default=None)
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True, default=None, unique=True)
    salary = models.DecimalField(verbose_name=_('Salary'), decimal_places=2, max_digits=8, validators=[MinValueValidator(0), MaxValueValidator(300_000)], blank=True, null=True, default=None)

    ## Groups
    rank = models.CharField(verbose_name=_('Rank'), choices=Rank.choices, max_length=15, blank=True, null=True, default=Rank.NORMAL)
    group = models.ManyToManyField(verbose_name=_('Group'), to='auth.Group', limit_choices_to={'name__startswith': 'contact'}, blank=True, default=None)

    class Meta:
        default_related_name = 'contact_person'
        app_label = 'contact'
        verbose_name = _('Person')
        verbose_name_plural = _('People')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    @property
    def addresses(self):
        return Address.objects.filter(contact=self)

    @property
    def phones(self):
        return Phone.objects.filter(contact=self)

    @property
    def age(self):
        SECOND = 1
        MINUTE = 60 * SECOND
        HOUR = 60 * MINUTE
        DAY = 24 * HOUR
        YEAR = 365.25 * DAY
        today = date.today()
        years = (today - self.birthday).total_seconds() / YEAR
        return round(years, 1)

    @property
    def changelog(self):
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.admin.models import LogEntry
        ct = ContentType.objects.get(app_label='contact', model='person')
        return LogEntry.objects.filter(content_type=ct, object_id=self.pk)
