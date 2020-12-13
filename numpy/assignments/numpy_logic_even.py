"""
* Assignment: Numpy Logic Even
* Filename: numpy_logic_even.py
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Set random seed to zero
    2. Generate ``data: np.ndarray`` of 9 random integers from 0 to 100 (exclusive)
    3. Check for even numbers which are less than 50 and save result to ``result``
    4. Check if all ``result`` matches this condition, result assing to `result_all`
    5. Check if any ``result`` matches this condition, result assign to `result_any`

Polish:
    1. Ustaw ziarno losowości na zero
    2. Wygeneruj ``data: np.ndarray`` z 9 losowymi liczbami całkowitymi od 0 do 100 (rozłącznie)
    3. Sprawdź parzyste elementy, które są mniejsze od 50 i wynik zapisz do ``result``
    4. Sprawdź czy wszystkie ``result`` spełniają ten warunek, wynik zapisz do `result_all`
    5. Sprawdź czy jakakolwiek ``result`` spełnia ten warunek, wynik zapisz do `result_any`

    >>> type(result) is np.ndarray
    True
    >>> type(data) is np.ndarray
    True
    >>> data
    array([44, 47, 64, 67, 67,  9, 83, 21, 36])
    >>> result
    array([ True, False, False, False, False, False, False, False,  True])
    >>> result_all
    False
    >>> result_any
    True
"""


# Given
import numpy as np
np.random.seed(0)


# Solution
data = np.random.randint(0, 100, size=9)
result = np.logical_and(data < 50, data % 2 == 0)
result_all = result.all()
result_any = result.any()
