   
test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()


def get_longest_word(line: str) -> str:
    tmp = line.split()
    result = tmp[0]
    for i in range(1, len(tmp)):
        if len(tmp[i]) > len(result):
            result = tmp[i]
    return result

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
