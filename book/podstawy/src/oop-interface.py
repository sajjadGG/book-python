class HttpInterface:
    def GET(self, url):
        raise NotImplementedError

    def POST(self, url):
        raise NotImplementedError


class OnlineClient(HttpInterface):
    pass


class OfflineClient(HttpInterface):
    pass



http = OnlineClient()
http.GET('http://python.astrotech.io')