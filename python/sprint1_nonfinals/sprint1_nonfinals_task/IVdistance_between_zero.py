# yandex_contest 69679095
def get_distances(plots, zero='0') -> list:
    results = [zero] * len(plots)
    zeros = [index for index, plot in enumerate(plots) if plot == zero]
    first, last = zeros[0], zeros[-1]
    results[:first] = [first - index for index in range(first)]
    for left, right in zip(zeros, zeros[1:]):
        results[left + 1:right] = [min(
            plot - left, right - plot) for plot in range(left + 1, right)]
    results[last + 1:] = [index - last for index in range(
        last + 1, len(plots))]
    return results


if __name__ == '__main__':
    input()
    print(*get_distances(input().split()))
