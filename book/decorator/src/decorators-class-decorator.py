class Cache(object):
    def __init__(self, function, max_hits=10, timeout=5):
        self.function = function
        self.max_hits = max_hits
        self.timeout = timeout
        self.cache = {}

    def __call__(self, *args):
        # Here the code returning the correct thing.
        print(self)


def cache_hits(max_hits=10, timeout=5):
    def _cache(function):
        return Cache(function, max_hits, timeout)
    return _cache


@cache_hits
def double(x):
    return x * 2

@cache_hits(max_hits=100, timeout=50)
def double(x):
    return x * 2


double()