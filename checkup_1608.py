from random import randint

lst = [randint(1, 10) for i in range(20)]
print(lst)

# for k, v in enumerate(lst):
#     print(k,v)
    
counter = {}
for elem in lst:
    counter[elem] = counter.get(elem, 0) + 1
print(counter)

# doubles = {}
# for key, value in counter.items():
#     if value > 1:
#         doubles[key] = value

doubles = {key: value for key, value in counter.items() if value > 1}


print(doubles)

lst1 = [* range(1,12)]

def avrg(arr, wnd):
    result = []
    current_sum = sum(arr[:wnd])
    result.append(current_sum / wnd)
    for i in range(len(arr) - wnd):
        current_sum -= arr[i]
        current_sum += arr[i + wnd]
        result.append(current_sum / wnd)
    return result

print(* avrg(lst1,4))


def twosum(arr, nmb):
    result = []
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == nmb:
            result.append(arr[left])
            result.append(arr[right])
            return result
        elif current_sum < nmb:
            left += 1
        else:
            right -= 1
            
print(twosum(lst, 11))

def twosum1(arr, nmb):
    result = []
    prevous = set()
    for elem in arr:
        y = nmb - elem
        if y in prevous:
            result.append(y)
            result.append(elem)
            return result
        else:
            prevous.add(elem)

print(twosum1(lst, 11))