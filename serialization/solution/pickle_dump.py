import json
import logging
import pickle

FILENAME_PICKLE = r'/tmp/addressbook.pickle'
FILENAME_JSON = r'/tmp/addressbook.json'

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class Contact:
    def __init__(self, first_name, last_name, phone=None, addresses=()):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.addresses = addresses

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.addresses}'

    def __repr__(self):
        return self.__str__()


class Addressbook:
    def __init__(self, **kwargs):
        # self.street = kwargs.get('street', None)
        # self.city = kwargs.get('city', None)
        for var, value in kwargs.items():
           setattr(self, var, value)

    def __str__(self):
        return f'{self.street} {self.city}'

    def __repr__(self):
        return self.__str__()


addressbook = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=[
        Addressbook(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Addressbook(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Addressbook(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Addressbook(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA', data_urodzenia=None),
    ]),
    Contact(first_name='José', last_name='Jiménez'),
    Contact(first_name='Иван', last_name='Иванович', addresses=[]),
]



log.debug(f'Addressbook: {addressbook}')


with open(FILENAME_PICKLE, mode='wb') as file:
    serialized = pickle.dumps(addressbook)
    file.write(serialized)


with open(FILENAME_PICKLE, mode='rb') as file:
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
        if dictionary.get('city'):
            return Addressbook(**dictionary)
        else:
            return Contact(**dictionary)


with open(FILENAME_JSON, 'w') as file:
    serialized = json.dumps(addressbook, cls=JSONObjectEncoder)
    file.write(serialized)


with open(FILENAME_JSON, 'r') as file:
    unserialized = json.loads(file.read(), cls=JSONObjectDecoder)
    log.debug(f'JSON: {unserialized}')
