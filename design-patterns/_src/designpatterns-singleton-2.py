class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(*args, **kwargs)
        obj = cls._instance
        obj.__init__()
        return obj


class MyClass(Singleton):
    pass
