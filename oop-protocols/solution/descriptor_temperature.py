class Temperature:
    class Value:
        def __set__(self, parent, new_value):
            if new_value < 0:
                raise ValueError('Negative temperature')
            else:
                parent._value = new_value

    def __init__(self):
        self.value = Temperature.Value()


t = Temperature()

t.value = 1
print(t.value)

t.value = -1
# ValueError: Negative temperature
