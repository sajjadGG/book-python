class Singleton:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(*args, **kwargs)
        obj = cls.instance
        obj.__init__()
        return obj


class MyClass(Singleton):
    pass
