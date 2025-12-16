#TypeAnnotation
"""
Bu özellikte değişkenlerin ve fonksiyonlarin tipleri belirtilir.
"""
def greet(name: str) -> str:
    return f"Hello, {name}!"

name: str = "Ali Miran"
print(greet(name))

def add_numbers(a: int, b: int) -> int:
    return a + b
a : int = 5
b : int = 10
print(add_numbers(a, b))
add_numbers(7, 78)
add_numbers(7.5, 8.2)  # Bu satır hata verecektir çünkü float tipindedir.
add_numbers("7", "8")  # Bu satır hata verecektir çünkü string tipindedir.
#add_numbers(7, "8")  # Bu satır hata verecektir çünkü biri int diğeri string tipindedir.
"""
yukarida degiskeni integer olarak belirttigimiz için sadece integer tipindeki verilerle işlem yapabiliriz.
"""

def process_value(value:int) -> int:
    if isinstance(value, int):
        return f"value is an integer: {value * 3}"
    else:
        return "value is not an integer"

print(process_value(12))
print(process_value("12"))  # Bu satır hata verecektir çünkü string tipindedir.

print("-------------------------------")

import numbers
from typing import List, Dict, Tuple, Union, Optional

def sum_list(numbers: List[Union[int, float]]) -> float:
    return sum(numbers)
numbers = [1, 2, 3.5, 4]
total = sum_list(numbers)
print("total:", total)