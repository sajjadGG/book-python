class range:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self._current_element = self.start
        return self

    def __next__(self):
        if self._current_element >= self.stop:
            raise StopIteration

        return_value = self._current_element
        self._current_element += self.step
        return return_value
