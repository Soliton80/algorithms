lst = [*range(1,13)]
A = [10, 10, 23, 10, 123, 66, 78, 123]

print(lst)

def middle(arr, av):
    result = []
    current_sum = sum(arr[:av])
    result.append(current_sum / av)
    for i in range(len(arr) - av):
        current_sum -= arr[i]
        current_sum += arr[i + av]
        result.append(current_sum / av)
    return result

print(middle(lst, 4))

def twosum(arr, num):
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if num == current_sum:
            result.append(arr[left])
            result.append(arr[right])
            return result
        if num > current_sum:
            left += 1
        else:
            right -= 1
    

print(twosum(lst, 16))
            
def twosum2(arr, num):
    result = []
    previos = set()
    for elem in arr:
        Y = num - elem
        if Y in previos:
            result.append(Y)
            result.append(elem)            
        else:
            previos.add(elem)
    return result
        
print(twosum2(lst, 16))

def countdict(arr):
    counter = {}
    for elem in arr:
        counter[elem] = counter.get(elem, 0) + 1
    # doubles = {elem: count for elem, count in counter.items() if count > 1}
    doubles = {}
    for elem, count in counter.items():
        if count > 1:
            doubles[elem] = count
    return doubles

print(countdict(A))
        
     