# yandex_contest 69678531
def get_distances(plots, zero='0') -> list:
    results = [zero] * len(plots)
    zeros = [index for index, plot in enumerate(plots) if plot == zero]
    first_zero, last_zero = zeros[0], zeros[-1]
    results[:first_zero] = [first_zero - index for index in range(first_zero)]
    for left, right in zip(zeros, zeros[1:]):
        results[left + 1:right] = [min(
            plot - left, right - plot) for plot in range(left + 1, right)]
    results[last_zero + 1:] = [index - last_zero for index in range(
        last_zero + 1, len(plots))]
    return results


if __name__ == '__main__':
    input()
    print(*get_distances(input().split()))
