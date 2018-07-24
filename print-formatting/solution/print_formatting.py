from typing import Union

STEP = 5
MAX = 41
MIN = -20


def celsius_to_fahrenheit(degree: Union[int, float]) -> float:
    return degree * 1.8 + 32


for celsius in range(MIN, MAX, STEP):
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f'Temperatura {celsius:=+8}C to {fahrenheit:_^+10.0f}F')
