class ReadCSV:
    __filename: str
    __delimiter: str
    __encoding: str
    __chunksize: int

    def __init__(self, filename):
        self.__filename = filename

    def withChunksize(self, value):
        self.__chunksize = value
        return self

    def withDelimiter(self, value):
        self.__delimiter = value
        return self

    def withEncoding(self, value):
        self.__encoding = value
        return self

if __name__ == '__main__':
    data = (
        ReadCSV('myfile.csv')
            .withChunksize(10_1000)
            .withDelimiter(',')
            .withEncoding('UTF-8')
    )
