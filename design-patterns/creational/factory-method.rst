Factory Method
==============


Rationale
---------
* EN: Factory Method
* PL: Metoda wytwórcza
* Type: class


Use Cases
---------


Design
------


Example
-------
.. code-block:: python

    class PDF:
        pass

    class Docx:
        pass

    class Document:
        def __new__(cls, *args, **kwargs):
            filename, extension = args[0].split('.')

            if extension == 'pdf':
                return PDF()
            elif extension == 'docx':
                return Docx()


    file1 = Document('myfile.pdf')
    file2 = Document('myfile.docx')

    print(file1)
    # <__main__.PDF object at 0x10f89afa0>

    print(file2)
    # <__main__.Docx object at 0x10f6fe9a0>

.. code-block:: python

    import os


    class HttpClientInterface:
        def GET(self):
            raise NotImplementedError

        def POST(self):
            raise NotImplementedError


    class GatewayLive(HttpClientInterface):
        def GET(self):
            """execute GET request over network"""

        def POST(self):
            """execute POST request over network"""


    class GatewayStub(HttpClientInterface):
        def GET(self):
            return {'firstname': 'José', 'lastname': 'Jiménez'}

        def POST(self):
            return {'status': 200, 'reason': 'OK'}


    class HttpClientFactory:
        instance = None

        def __new__(cls, *args, **kwargs):
            if not cls.instance:
                if os.getenv('ENVIRONMENT') == 'production':
                    cls.instance = GatewayLive()
                else:
                    cls.instance = GatewayStub()

            return cls.instance


    client = HttpClientFactory()
    result = client.GET()
    print(result)


    client2 = HttpClientFactory()
    result1 = client2.GET()
    result2 = client2.POST()

    print(result1)
    print(result2)

.. code-block:: python

    class Document:
        extension = None

        def __new__(cls, filename, *args, **kwargs):
            name, extension = filename.split('.')
            for cls in Document.__subclasses__():
                if cls.extension == extension:
                    return super().__new__(cls)
            else:
                raise NotImplementedError('File format unknown')


    class PDF(Document):
        extension = 'pdf'

    class Txt(Document):
        extension = 'txt'

    class Word(Document):
        extension = 'docx'


    file = Document('myfile.txt')
    print(type(file))
    # <class '__main__.Txt'>

    file = Document('myfile.pdf')
    print(type(file))
    # <class '__main__.PDF'>

.. code-block:: python

    class ConfigParserInterface:
        extension = None

        def __init__(self, filename):
            self.filename = filename

        def read(self):
            with open(self.filename) as file:
                content = file.read()
                return self.parse(content)

        def parse(self, content):
            return NotImplementedError


    class ConfigParserINI(ConfigParserInterface):
        extension = '.ini'

        def parse(self, content):
            print('Parsing INI file')

    class ConfigParserCSV(ConfigParserInterface):
        extension = '.csv'

        def parse(self, content):
           print('Parsing CSV file')

    class ConfigParserYAML(ConfigParserInterface):
        extension = '.yaml'

        def parse(self, content):
           print('Parsing YAML file')

    class ConfigFileJSON(ConfigParserInterface):
        extension = '.json'

        def parse(self, content):
           print('Parsing JSON file')


    class ConfigFileXML(ConfigParserInterface):
        extension = '.xml'

        def parse(self, content):
           print('Parsing XML file')


    def config_parser_factory(filename):
        import os
        parsers = {p.extension: p for p in ConfigParserInterface.__subclasses__()}
        extension = os.path.splitext(filename)[1]

        try:
            return parsers[extension](filename)
        except KeyError:
            raise NotImplementedError


     # iris.csv or *.csv, *.json *.yaml...
    filename = input('Type filename: ')

    config_parser = config_parser_factory(filename)
    config_parser.read()

.. code-block:: python

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        cls = {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'virginica': Virginica,
        }.get(species, None)

        if not cls:
            raise NotImplementedError

        return cls

    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        return {
            'setosa': Setosa,
            'versicolor': Versicolor,
            'virginica': Virginica,
        }.get(species, None)

    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    import sys


    class Setosa:
        pass

    class Versicolor:
        pass

    class Virginica:
        pass

    def factory(species):
        try:
            CURRENT_MODULE = sys.modules[__name__]
            return getattr(CURRENT_MODULE, species.capitalize())
        except AttributeError:
            raise NotImplementedError


    iris = factory('setosa')
    print(iris)
    # <class '__main__.Setosa'>

.. code-block:: python

    from abc import ABCMeta, abstractmethod

    class Path(metaclass=ABCMeta):
        def __new__(cls, path, *args, **kwargs):
            if path.startswith(r'C:\Users'):
                instance = object.__new__(WindowsPath)
            if path.startswith('/home'):
                return object.__new__(LinuxPath)
            if path.startswith('/Users'):
                return object.__new__(macOSPath)
            instance.__init__(path)
            return instance

        def __init__(self, filename):
            self.filename = filename

        @abstractmethod
        def dir_create(self):
            pass

        @abstractmethod
        def dir_list(self):
            pass

        @abstractmethod
        def dir_remove(self):
            pass


    class WindowsPath(Path):
        def dir_create(self):
            pass

        def dir_list(self):
            pass

        def dir_remove(self):
            pass


    class LinuxPath(Path):
        def dir_create(self):
            pass

        def dir_list(self):
            pass

        def dir_remove(self):
            pass


    class macOSPath(Path):
        def dir_create(self):
            pass

        def dir_list(self):
            pass

        def dir_remove(self):
            pass


    file = Path(r'C:\Users\MWatney\myfile.txt')
    print(type(file))
    # <class '__main__.WindowsPath'>

    file = Path(r'/home/mwatney/myfile.txt')
    print(type(file))
    # <class '__main__.LinuxPath'>

    file = Path(r'/Users/mwatney/myfile.txt')
    print(type(file))
    # <class '__main__.macOSPath'>


Assignments
-----------
.. todo:: Create assignments

