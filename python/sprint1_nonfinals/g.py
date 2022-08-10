test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()


def to_binary(number: int) -> str:
    binnum = ''
    while number > 0:
        binnum = str(number % 2) + binnum
        number = number // 2
    return binnum

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))