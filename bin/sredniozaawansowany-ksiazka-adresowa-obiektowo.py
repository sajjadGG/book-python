import json
import logging
import pickle

KSIAZKA_ADRESOWA_PICKLE = '/tmp/ksiazka-adresowa.pickle'

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Kontakt:
    def __init__(self, imie, nazwisko, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adresy}'

    def __repr__(self):
        return self.__str__()


class Adres:
    def __init__(self, **kwargs):
        self.ulica = kwargs.get('ulica', None)
        self.miasto = kwargs.get('miasto', None)

    def __str__(self):
        return f'{self.ulica} {self.miasto}'

    def __repr__(self):
        return self.__str__()


ksiazka_adresowa = [
    Kontakt(imie='Matt', nazwisko='Harasymczuk', adresy=[
        Adres(ulica='ulica1', miasto='miasto1'),
        Adres(ulica='ulica2', miasto=''),
        Adres(ulica='ulica3'),
    ]),
    Kontakt(imie='Al', nazwisko='Shepard'),
    Kontakt(imie='José', nazwisko='Jiménez', adresy=[]),
]

log.debug(f'Ksiażka adresowa: {ksiazka_adresowa}')


with open(KSIAZKA_ADRESOWA_PICKLE, 'wb') as file:
    serialized = pickle.dumps(ksiazka_adresowa)
    file.write(serialized)


with open(KSIAZKA_ADRESOWA_PICKLE, 'rb') as file:
    unserialized = pickle.loads(file.read())
    log.debug(f'Pickle: {unserialized}')


class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            return obj.__dict__


class JSONObjectDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_object)

    def decode_object(self, dictionary):
        if dictionary.get('ulica'):
            return Adres(**dictionary)
        else:
            return Kontakt(**dictionary)


with open('/tmp/ksiazka-adresowa.json', 'w') as file:
    serialized = json.dumps(ksiazka_adresowa, cls=JSONObjectEncoder)
    file.write(serialized)


with open('/tmp/ksiazka-adresowa.json', 'r') as file:
    unserialized = json.loads(file.read(), cls=JSONObjectDecoder)
    log.debug(f'JSON: {unserialized}')
