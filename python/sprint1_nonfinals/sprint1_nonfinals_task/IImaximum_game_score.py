# yandex_contest 69674720
def maximum_scores(capacity: int, push_keys, gamers: int = 2,
                   permited_keys='123456789') -> int:
    return sum(push_keys.count(elem) <= capacity*gamers
               for elem in permited_keys if push_keys.count(elem))


if __name__ == '__main__':
    print(maximum_scores(int(input()),
                         (f'{input()}{input()}{input()}{input()}')))
