test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()

from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    for elem in longer:
        if elem not in shorter:
            return elem
    else:
        longer = sorted(longer)
        shorter = sorted(shorter)
        for i in range(len(longer)):
            if longer.count(longer[i]) > shorter.count(shorter[i]):
                return longer[i]

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))

# print(sorted(shorter))
# print(sorted(longer))
