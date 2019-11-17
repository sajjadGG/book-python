import os
from dataclasses import dataclass, field
from hashlib import sha1
from datetime import timedelta, datetime
from http import HTTPStatus
from typing import Dict

import requests


class CacheInterface:
    def _get_location(self, key: str) -> str:
        raise NotImplementedError

    def get(self, key: str) -> str:
        raise NotImplementedError

    def set(self, key: str, value: str) -> None:
        raise NotImplementedError

    def clear(self, key: str) -> None:
        raise NotImplementedError

    def is_valid(self, key: str) -> bool:
        raise NotImplementedError


@dataclass
class CacheMemory(CacheInterface):
    expiration: timedelta = timedelta(seconds=30)
    _data: Dict[str, str] = field(default_factory=dict)

    def is_valid(self, key: str) -> bool:
        if key in self._data:
            return True
        else:
            return False

    def set(self, key: str, value: str) -> None:
        self._data[key] = value

    def get(self, key: str) -> str:
        return self._data[key]


@dataclass
class CacheFilesystem(CacheInterface):
    location: str = "/tmp/cache/"
    expiration: timedelta = timedelta(seconds=30)

    def __post_init__(self):
        if os.path.isfile(self.location):
            os.remove(self.location)

        if not os.path.isdir(self.location):
            os.makedirs(self.location, exist_ok=True)

    def _get_location(self, key: str) -> str:
        filename = sha1(key.encode()).hexdigest()
        return os.path.join(self.location, filename)

    def is_valid(self, key: str) -> bool:
        location = self._get_location(key)

        if not os.path.isfile(location):
            return False

        timestamp = os.path.getmtime(location)
        modification_date = datetime.fromtimestamp(timestamp)
        last_update = datetime.now() - modification_date

        if last_update < self.expiration:
            return True
        else:
            return False

    def get(self, key: str) -> str:
        location = self._get_location(key)

        with open(location) as file:
            return file.read()

    def set(self, key: str, value: str) -> None:
        location = self._get_location(key)

        with open(location, mode="w") as file:
            file.write(value)


@dataclass
class HTTPGateway:
    _cache: CacheInterface = CacheMemory

    def get(self, url):
        if self._cache.is_valid(url):
            return self._cache.get(url)
        else:
            data = self._fetch(url)
            self._cache.set(url, data)
            return data

    def _fetch(self, url):
        response = requests.get(url)

        if response.status_code == HTTPStatus.OK:
            return response.text
        else:
            raise ConnectionError()


@dataclass
class CacheDatabase(CacheInterface):
    location: str


if __name__ == "__main__":
    cache = CacheFilesystem(location="/tmp/cache/", expiration=timedelta(seconds=1))
    http = HTTPGateway(cache)

    URL = "https://github.com/AstroMatt/book-python/blob/master/numerical-analysis/data/iris-dirty.csv"
    data = http.get(URL)
    print(data)


if __name__ == '__main__':
    database = CacheDatabase(location='sqlite3://http-cache.sqlite3')
    filesystem = CacheFilesystem(location='/tmp/http-cache.txt')
    memory = CacheMemory(expiration=timedelta(hours=2))

    http1 = HTTPGateway(_cache=database)
    http1.get('http://python.astrotech.io')

    http2 = HTTPGateway(_cache=filesystem)
    http2.get('http://python.astrotech.io')

    http3 = HTTPGateway(_cache=memory)
    http3.get('http://python.astrotech.io')
