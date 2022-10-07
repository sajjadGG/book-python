class Borg:
    shared_state: dict = {}

    def __init__(self):
        self.__dict__ = self.shared_state
