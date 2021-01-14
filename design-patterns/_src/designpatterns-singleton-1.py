class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = ...
        return cls.__instance


# Creating first instance for the first time
first = Singleton.get_instance()

# Connecting for the second time
# Will use existing instance
second = Singleton.get_instance()
