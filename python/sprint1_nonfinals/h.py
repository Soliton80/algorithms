test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()

from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    
    max_len = max(len(first_number), len(second_number))
    
    first_number = first_number.zfill(max_len)
    second_number = second_number.zfill(max_len)
    
    result = ''
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if first_number[i] == '1' else 0
        r += 1 if second_number[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
    
        carry = 0 if r < 2 else 1
    
    if carry != 0:
        result = '1' + result
    
    return result.zfill(max_len)

def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
