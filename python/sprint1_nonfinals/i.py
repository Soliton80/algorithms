test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()


from math import log


def is_power_of_four(number: int) -> bool:
    if log(number,4) % 1 == 0:
        return True
    return False

print(is_power_of_four(int(input())))
