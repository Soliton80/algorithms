# yandex_contest 69676793
def maximum_scores(capacity: int, push_keys, gamers: int = 2,
                   permited_keys='123456789') -> int:
    return sum(
        push_keys.count(elem) <= capacity * gamers
        for elem in permited_keys if elem in push_keys
        )


if __name__ == '__main__':
    print(maximum_scores(
        int(input()),
        f'{input()}{input()}{input()}{input()}'
        ))
