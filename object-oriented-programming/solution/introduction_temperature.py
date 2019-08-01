class Temperature:
    def __init__(self, value):
        self.value = value


celsius = Temperature(36.6)
fahrenheit = Temperature(97.88)
kelvin = Temperature(309.75)

print(celsius.value)
print(fahrenheit.value)
print(kelvin.value)
