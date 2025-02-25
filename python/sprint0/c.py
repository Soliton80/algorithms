from typing import List, Tuple

def moving_average(arr: List[int], window_size: int) -> List[float]:
    result = []
    sum_array = sum(arr[:window_size])
    result.append(sum_array / window_size)
    for i in range(len(arr) - window_size ):
        sum_array -= arr[i]
        sum_array += arr[i + window_size]
        result.append(sum_array / window_size)
    return result
    
def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))


# from typing import List, Tuple

# def moving_average(arr: List[int], window_size: int) -> List[float]:
#     result = []
#     for begin_index in range(len(arr)-window_size + 1):
#         end_index = begin_index + window_size
#         current_sum = 0
#         for i in arr[begin_index:end_index]:
#             current_sum += i 
#         current_avg = current_sum / window_size
#         result.append(current_avg)
#     return result

# def read_input() -> Tuple[List[int], int]:
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     window_size = int(input())
#     return arr, window_size

# arr, window_size = read_input()
# print(" ".join(map(str, moving_average(arr, window_size))))

