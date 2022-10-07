from abc import ABC, abstractmethod
from dataclasses import dataclass


class Stream(ABC):
    @abstractmethod
    def write(self, data: str) -> None:
        pass


class CloudStream(Stream):
    def write(self, data: str) -> None:
        print(f'Storing: "{data}"')


@dataclass
class EncryptedCloudStream(Stream):
    stream: Stream

    def write(self, data: str) -> None:
        encrypted: str = self._encrypt(data)
        self.stream.write(encrypted)

    def _encrypt(self, data: str) -> str:
        return '3817f443b81e986d8e2771c6bf5e744e7ec0e844'


@dataclass
class CompressedCloudStream(Stream):
    stream: Stream

    def write(self, data: str) -> None:
        compressed: str = self._compress(data)
        self.stream.write(compressed)

    def _compress(self, data: str) -> str:
        return data[0:10]


if __name__ == '__main__':
    credit_card_number = '1234-1234-1234-1234'

    cloud_steam = CloudStream()
    cloud_steam.write(credit_card_number)
    # Storing: "Data"

    cloud_steam = EncryptedCloudStream(CloudStream())
    cloud_steam.write(credit_card_number)
    # Storing: "3817f443b81e986d8e2771c6bf5e744e7ec0e844"

    cloud_steam = EncryptedCloudStream(CompressedCloudStream(CloudStream()))
    cloud_steam.write(credit_card_number)
    # Storing: "3817f443b8"
