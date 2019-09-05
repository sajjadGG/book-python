class KelvinTemperature:
    class Value:
        def __set__(self, parent, new_value):
            if new_value < 0:
                raise ValueError('Negative temperature')
            else:
                parent._value = new_value

    value = Value()


temp = KelvinTemperature()

temp.value = 1
print(temp.value)

temp.value = -1
# ValueError: Negative temperature
