class Borg:
    __shared_state: dict = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
