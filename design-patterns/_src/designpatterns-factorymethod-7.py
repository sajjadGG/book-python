import os


class HttpClientInterface:
    def GET(self):
        raise NotImplementedError

    def POST(self):
        raise NotImplementedError


class GatewayLive(HttpClientInterface):
    def GET(self):
        print('Execute GET request over network')
        return ...

    def POST(self):
        print('Execute POST request over network')
        return ...


class GatewayStub(HttpClientInterface):
    def GET(self):
        print('Returning stub GET')
        return {'firstname': 'Mark', 'lastname': 'Watney'}

    def POST(self):
        print('Returning stub POST')
        return {'status': 200, 'reason': 'OK'}


class HttpGatewayFactory:
    def __new__(cls, *args, **kwargs):
        if os.getenv('ENVIRONMENT') == 'production':
            return GatewayLive()
        else:
            return GatewayStub()


os.environ['ENVIRONMENT'] = 'testing'

client = HttpGatewayFactory()
result = client.GET()
# Returning stub GET
result = client.POST()
# Returning stub POST

os.environ['ENVIRONMENT'] = 'production'

client = HttpGatewayFactory()
result = client.GET()
# Execute GET request over network
result = client.POST()
# Execute POST request over network
