# yandex_contest 69667413
def maximum_scores(capacity: int, push_keys, gamers: int = 2) -> int:
    permited_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return sum(True for score in (push_keys.count(elem)
                                  for elem in set(push_keys)
                                  if elem in permited_keys)
               if score <= capacity * gamers)


if __name__ == '__main__':
    print(maximum_scores(int(input()),
                         (f'{input()}{input()}{input()}{input()}')))
