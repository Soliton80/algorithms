from typing import List, Tuple

def zipper(a: List[int], b: List[int]) -> List[int]:
    # Здесь реализация вашего решения
    t = []
    for i in range(len(a)):
        t.append(a[i])
        t.append(b[i])
    return t

def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b

a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
