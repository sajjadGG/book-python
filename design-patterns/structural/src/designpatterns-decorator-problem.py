class CloudStream:
    def write(self, data: str) -> None:
        print(f'Storing: "{data}"')


class EncryptedCloudStream(CloudStream):
    def write(self, data: str) -> None:
        encrypted: str = self.__encrypt(data)
        super().write(encrypted)

    def __encrypt(self, data: str) -> str:
        return '3817f443b81e986d8e2771c6bf5e744e7ec0e844'


class CompressedCloudStream(CloudStream):
    def write(self, data: str) -> None:
        compressed = self.__compress(data)
        super().write(compressed)

    def __compress(self, data: str) -> str:
        return data[0:10]


if __name__ == '__main__':
    cloud_steam = CloudStream()
    cloud_steam.write('Data')
    # Storing: "Data"

    cloud_steam = EncryptedCloudStream()
    cloud_steam.write('Data')
    # Storing: "3817f443b81e986d8e2771c6bf5e744e7ec0e844"
