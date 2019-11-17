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


class Address:
    def __init__(self, **kwargs):
        # self.location = kwargs.get('location', None)
        # self.city = kwargs.get('city', None)
        for var, value in kwargs.items():
           setattr(self, var, value)

    def __str__(self):
        return f'{self.location} {self.city}'

    def __repr__(self):
        return self.__str__()


INPUT = [
    Contact(first_name='Jan', last_name='Twardowski', addresses=(
        Address(location='Johnson Space Center', city='Houston, TX'),
        Address(location='Kennedy Space Center', city='Merritt Island, FL'),
        Address(location='Jet Propulsion Laboratory', city='Pasadena, CA'),
    )),
    Contact(first_name='Mark', last_name='Watney'),
    Contact(first_name='Melissa', last_name='Lewis', addresses=()),
]


with open(FILENAME_PICKLE, mode='wb') as file:
    serialized = pickle.dumps(INPUT)
    file.write(serialized)


with open(FILENAME_PICKLE, mode='rb') as file:
    unserialized = pickle.loads(file.read())
    log.debug(f'Pickle: {unserialized}')
    # [
    #     Jan Twardowski (
    #         Johnson Space Center Houston, TX,
    #         Kennedy Space Center Merritt Island, FL
    #         Jet Propulsion Laboratory Pasadena, CA
    #     ),
    #     Mark Watney (),
    #     Melissa Lewis ()
    # ]




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
            return Address(**dictionary)
        else:
            return Contact(**dictionary)


with open(FILENAME_JSON, 'w') as file:
    serialized = json.dumps(INPUT, cls=JSONObjectEncoder)
    file.write(serialized)


with open(FILENAME_JSON, 'r') as file:
    unserialized = json.loads(file.read(), cls=JSONObjectDecoder)
    log.debug(f'JSON: {unserialized}')
    # [
    #     Jan Twardowski [
    #         Johnson Space Center Houston, TX,
    #         Kennedy Space Center Merritt Island, FL
    #         Jet Propulsion Laboratory Pasadena, CA
    #     ],
    #     Mark Watney [],
    #     Melissa Lewis []
    # ]
