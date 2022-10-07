from abc import ABC, abstractproperty, abstractmethod
from dataclasses import dataclass


@dataclass
class ConfigParser(ABC):
    filename: str

    @abstractproperty
    @property
    def extension(self):
        pass

    def show(self):
        content = self.read()
        return self.parse(content)

    @abstractmethod
    def parse(self, content: str) -> dict:
        return NotImplementedError

    def read(self):
        with open(self.filename) as file:
            return file.read()

    def __new__(cls, filename, *args, **kwargs):
        _, extension = filename.split('.')
        for parser in cls.__subclasses__():
            if parser.extension == extension:
                instance = super().__new__(parser)
                instance.__init__(filename)
                return instance
        else:
            raise NotImplementedError('Parser for given file type not found')


class ConfigParserINI(ConfigParser):
    extension = 'ini'

    def parse(self, content: str) -> dict:
        print('Parsing INI file')


class ConfigParserCSV(ConfigParser):
    extension = 'csv'

    def parse(self, content: str) -> dict:
        print('Parsing CSV file')


class ConfigParserYAML(ConfigParser):
    extension = 'yaml'

    def parse(self, content: str) -> dict:
        print('Parsing YAML file')


class ConfigFileJSON(ConfigParser):
    extension = 'json'

    def parse(self, content: str) -> dict:
        print('Parsing JSON file')


class ConfigFileXML(ConfigParser):
    extension = 'xml'

    def parse(self, content: str) -> dict:
        print('Parsing XML file')


if __name__ == '__main__':
    # iris.csv or *.csv, *.json *.yaml...
    # filename = input('Type filename: ')
    config = ConfigParser('/tmp/myfile.json')
    config.show()
