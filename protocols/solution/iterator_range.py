for character in 'python':
    print(character)

for number in [1, 2, 3, 4]:
    print(number)

for key, value in [(0, 0), (1, 1), (1, 2)]:
    print('%s -> %s' % (key, value))

dictionary = {'x': 1, 'y': 2}

for key in dictionary:
    print(dictionary.get(key))


class Figures:
    storage = []
    current_element = 0

    def __iter__(self):
        return self

    def push(self, figure):
        self.storage.append(figure)

    def next(self):
        self.current_element += 1
        return self.storage[self.current_element]
