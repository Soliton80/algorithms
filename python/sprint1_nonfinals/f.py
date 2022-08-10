test_file = open('python/sprint1_nonfinals/input.txt')
def input() -> str:
    return test_file.readline()

def is_palindrome(line: str) -> bool:
    line = ''.join(i for i in line if i.isalnum()).lower()
    if line == line[::-1]:
        return True
    return False

print(is_palindrome(input().strip()))
