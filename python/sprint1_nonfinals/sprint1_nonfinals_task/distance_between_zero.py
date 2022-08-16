# 69667209
def get_distances(plots, zero='0') -> list:
    results = [zero] * len(plots)
    lowest_tmp_result = float('inf')
    for index, plot in enumerate(plots):
        if plot == zero:
            results[index] = 0
            lowest_tmp_result = 0
            for pos in range(index, -1, -1):
                if lowest_tmp_result <= results[pos]:
                    results[pos] = lowest_tmp_result
                    lowest_tmp_result += 1
                else:
                    break
            lowest_tmp_result = 0
        else:
            lowest_tmp_result += 1
            results[index] = lowest_tmp_result
    return results


if __name__ == '__main__':
    input()
    print(* get_distances(input().split()))
