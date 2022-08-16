# yandex_contest 69667347
def get_distances(plots, zero='0') -> list:
    results = [zero] * len(plots)
    zeros = [index for index, plot in enumerate(plots) if plot == zero]
    first_zero = zeros[0]
    last_zero = zeros[-1]
    for index in range(first_zero):
        results[index] = first_zero - index
    for index in range(1, len(zeros)):
        first_zero = zeros[index - 1]
        for pos in range(first_zero, zeros[index]):
            results[pos] = min(pos - first_zero, zeros[index] - pos)
    for index in range(last_zero, len(plots)):
        results[index] = index - last_zero
    return results


if __name__ == '__main__':
    input()
    print(* get_distances(input().split()))
