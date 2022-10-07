class Singleton:
    instance = None

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = ...
        return cls.instance


# Creating first instance for the first time
first = Singleton.get_instance()

# Connecting for the second time
# Will use existing instance
second = Singleton.get_instance()
