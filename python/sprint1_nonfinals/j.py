test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()

from typing import List
import math


def factorize(number: int) -> List[int]:
    result = []
    while number % 2 == 0:
        result.append(2)
        number = number / 2
        
    for i in range(3,int(math.sqrt(number)) +1, 2):         
        while (number % i == 0):
            result.append(i)
            number = number / i
    
    if number > 2:
        result.append(number)

    return map(int, result)
         

result = factorize(int(input()))
print(" ".join(map(str, result)))
