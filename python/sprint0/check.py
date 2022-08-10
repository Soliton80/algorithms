# from random import randint

# lst = [randint(0,20) for i in range(20)]
# print(lst)

# def avg(arr, wnd):
#     result = []
#     current_sum = sum(arr[:wnd])
#     result.append(current_sum/wnd)
#     for i in range(len(arr) - wnd):
#         current_sum -= arr[i]
#         current_sum += arr[i+wnd]
#         result.append(current_sum/wnd)
#     return result


# print(avg(lst,4))

# def Twosum(arr, checknumber):
#     result = []
#     arr.sort()
#     left = 0
#     right = len(arr) -1 
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == checknumber:
#             result.append(arr[left])
#             result.append(arr[right])
#             return result
#         elif current_sum < checknumber:
#             left += 1
#         elif current_sum > checknumber:
#             right -= 1
#     return None


# print(Twosum(lst,12))

# def Twosum2(arr, checknumber):
#     result = []
#     previous = set()
#     for i in arr:
#         y = checknumber - i
#         if y in previous:
#             result.append(y)
#             result.append(i)
#             return result
#         else:
#             previous.add(i)
#     return None


# print(Twosum2(lst,12))


# def mymax(arr):
#     fn = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > fn:
#             fn = arr[i]
#     return fn


# def myminsort(arr):
#     result = []
#     while arr:
#         result.insert(0,mymax(arr))
#         arr.remove(mymax(arr))
#     return result

# print(myminsort(lst))

# print(lst)

import time

time_start = time.time()
i = 0
while i < 1000000000:
    # Do nothing
    i += 1

time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')