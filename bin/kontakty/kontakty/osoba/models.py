from django.db import models


class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    #dataurodzenia = models.DateTimeField()


    def __str__(self):
        return '{imie} {nazwisko}'.format(**self.__dict__)


class Adres(models.Model):
    osoba = models.ForeignKey(to='osoba.Osoba')
    ulica = models.CharField(max_length=50)
    numer = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{ulica} {numer}'.format(**self.__dict__)

