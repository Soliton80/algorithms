# yandex_contest 69674704
def get_distances(plots, zero='0') -> list:
    results = [zero] * len(plots)
    zeros = [index for index, plot in enumerate(plots) if plot == zero]
    first_zero, last_zero = zeros[0], zeros[-1]
    for index in range(first_zero):
        results[index] = first_zero - index
    for index in range(1, len(zeros)):
        first_zero, last_zero = zeros[index - 1], zeros[index]        
        for pos in range(first_zero + 1, last_zero):
            results[pos] = min(pos - first_zero, last_zero - pos)
    for index in range(last_zero + 1, len(plots)):
        results[index] = index - last_zero
    return results


if __name__ == '__main__':
    input()
    print(* get_distances(input().split()))
