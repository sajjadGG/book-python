from django.db import models
from django.utils.translation import ugettext_lazy as _


class Adres(models.Model):
    TYPY = [
        ('praca', _('Praca')),
        ('prywatny', _('Prywatny')),
    ]

    kontakt = models.ForeignKey('kontakt.Kontakt')
    ulica = models.CharField(max_length=50)
    nr_domu = models.CharField(max_length=5)
    nr_mieszkania = models.CharField(max_length=5, blank=True, null=True)
    miejscowosc = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=50)
    typ = models.CharField(max_length=20, choices=TYPY)


class Kontakt(models.Model):
    imie = models.CharField(max_length=30, verbose_name=_('Imie'))
    nazwisko = models.CharField(max_length=50, db_index=True)
    telefon = models.IntegerField(db_index=True)
    zdjecie = models.FileField(blank=True, null=True)
    data_urodzenia = models.DateField()
    komentarz = models.TextField(blank=True, null=True)
    jest_adminem = models.BooleanField()

    def __str__(self):
        return '{imie} {nazwisko}'.format(
            imie=self.imie,
            nazwisko=self.nazwisko,
        )

    class Meta:
        verbose_name = _('Kontakt')
        verbose_name_plural = _('Kontakty')
