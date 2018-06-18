class ConfigParserInterface:
    extension = None

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as file:
            return file.read()

    def parse(self):
        return NotImplementedError


class ConfigParserINI(ConfigParserInterface):
    extension = '.ini'

    def parse(self):
        print('Parsing INI file')
        return dict(...)

class ConfigParserCSV(ConfigParserInterface):
    extension = '.csv'

    def parse(self):
       print('Parsing CSV file')
       return dict()

class ConfigParserYAML(ConfigParserInterface):
    extension = '.yaml'

    def parse(self):
       print('Parsing YAML file')
       return dict()

class ConfigFileJSON(ConfigParserInterface):
    extension = '.json'

    def parse(self):
       print('Parsing JSON file')
       return dict()


class ConfigFileXML(ConfigParserInterface):
    extension = '.xml'

    def parse(self):
       print('Parsing XML file')
       return dict()


def config_parser_factory(filename):
    import os
    parsers = {p.extension: p for p in ConfigParserInterface.__subclasses__()}
    extension = os.path.splitext(filename)[1]

    try:
        return parsers[extension](filename)
    except KeyError:
        raise NotImplementedError


filename = input('Type filename: ')  # iris.csv or *.csv, *.json *.yaml...
parser = config_parser_factory()
config = parser.parse(filename)