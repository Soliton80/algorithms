from random import randint

lst = [randint(1,20) for i in range(1,20)]
lst1 = [*range(12)]

print(lst)

def twosum(arr,quees):
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 2
    while left < right:
        if arr[left] + arr[right] == quees:
            result.append(arr[left])
            result.append(arr[right])
            return result
        if quees > arr[left] + arr[right] :
            left += 1
        else:
            right -= 1
            

print(twosum(lst,12))


def twosum2(arr, quessnum):
    result = []
    previous = set()
    for elem in arr:
        y = quessnum - elem
        if y in previous:
            result.append(y)
            result.append(elem)
            return result
        else:
            previous.add(elem)
    
            
print(twosum2(lst,12))


def mediavg(arr,wnd):
    result = []
    current_sum = sum(arr[:wnd])
    result.append(current_sum / wnd)
    for i in range(0, len(arr) - wnd):
        current_sum -= arr[i]
        current_sum += arr[i + wnd]
        result.append(current_sum / wnd)
    return result

print(mediavg(lst1, 4))

# counter = {}
# for elem in lst:
#     counter[elem] = counter.get(elem, 0) + 1
# print(counter)


"""counterdict = {key:value for lst[key], lst.get(value, 0) in lst }


for elem in arr:
    counter[elem] = counter.get(elem, 0) + 1
    # doubles = {elem: count for elem, count in counter.items() if count > 1}

a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}"""
            
        