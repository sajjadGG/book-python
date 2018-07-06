class HttpClientInterface:
    def GET(self):
        raise NotImplementedError

    def POST(self):
        raise NotImplementedError


class GatewayLive(HttpClientInterface):
    def GET(self):
        # zaciagnij informacje o userze
        return ...

    def POST(self):
        # zapytaj po sieci
        pass


class GatewayStub(HttpClientInterface):
    def GET(self):
        return {'imie': 'nazwisko'}


class HttpClientFactory:
    instance = None

    def __init__(self):
        if HttpClientFactory.instance:
            HttpClientFactory.instance = GatewayStub

        return HttpClientFactory.instance


client = HttpClientFactory()
client.GET()

client2 = HttpClientFactory()
client2.GET()
client2.POST()