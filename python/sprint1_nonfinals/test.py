# test_file = open('python/sprint1_nonfinals/input.txt')
# def input() -> str:
#     return test_file.readline()

# def get_distance(nmbrs_lst: list) -> list:


#     # Создать выходной список и заполнить нулями.
#     answer = [0] * len(nmbrs_lst)

#     # Получить позиции всех нулевых в виде списка.
#     zeros = [i for i, v in enumerate(nmbrs_lst) if v == 0]
#     print(zeros)
#     print(zeros[-1])


#     # Создать простой цикл по позициям домов "до первого нулевого".
#     for i in range(zeros[0]):
#         # Сохранить результат явной формулы для расстояния между домом и первым нулевым.
#         answer[i] = zeros[0] - i

#     # Создать цикл по парам соседних нулевых.
#     for k in range(1, len(zeros)):
#         # Внутри него простой цикл по всем домам "между этой парой".
#         for i in range(zeros[k - 1] + 1, zeros[k]):
#             # Сохранить результат явной формулы для минимального расстояния между домом и этими нулевыми.
#             answer[i] = min(i - zeros[k - 1], zeros[k] - i) 

#     # Создать простой цикл по позициям домов "после последнего нулевого".
#     for i in range(zeros[-1] + 1, len(nmbrs_lst)):
#         # Сохранить результат явной формулы для расстояния между домом и последним нулевым.
#         answer[i] = i - zeros[-1]

#     return answer



# if __name__ == '__main__':

#     def read_input():
#         n = int(input())
#         nmbrs_lst = list(map(int, input().strip().split()))
#         return nmbrs_lst

#     nmbrs_lst = read_input()

#     print(nmbrs_lst)
#     print(*get_distance(nmbrs_lst))
