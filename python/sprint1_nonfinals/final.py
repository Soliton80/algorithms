test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()

from typing import List, Tuple

def count_len(start, numbers_list):
    d = start
    for n in numbers_list:
        if n == '0':
            d = 0
        else:
            d += 1
        yield d

def get_distance(numbers_list: str, length: int) -> List[int]:
    result = []
      
    left = count_len(numbers_list, length)
    right = reversed(tuple(count_len(reversed(numbers_list), length)))
    
    for pair in zip(left, right):
        result.append(min(pair))
    
    return result



def read_input() -> Tuple[int, str]:
    length = int(input().strip())
    numbers_list = input().split() 
    return  length, numbers_list


length, numbers_list = read_input()

# print(get_distance(numbers_list, length))

print(" ".join(map(str, get_distance(numbers_list, length))))