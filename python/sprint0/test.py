def get_max(a,b,c):
    find_number = a
    if b > find_number:
        find_number = b
    if c > find_number:
        find_number = c
    return find_number


from random import randint
alist = [randint(1,10) for i in range(12)]
print(alist)

def maxvalue(alist):
    maxnumber = alist[0]
    for i in range(1, len(alist)):
        if alist[i] > maxnumber:
            maxnumber = alist[i]
    return maxnumber

print(maxvalue(alist))

alist1 = list(alist)
alist2 = alist[::]
alist3 = alist.copy()
alist3.sort()
print(alist3)


def mymaxsort(alist):
    newlst = []
    while alist:
        newlst.append(maxvalue(alist))
        alist.remove(maxvalue(alist))
    return newlst

print(mymaxsort(alist))

def myminsort(alist):
    newlst = []
    while alist:
        newlst.insert(0, maxvalue(alist))
        alist.remove(maxvalue(alist))
    return newlst

print(myminsort(alist1))


def gettwosum(arr, number):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == number:
                result.append(arr[i])
                result.append(arr[j])
                return result
    return None

print(gettwosum(alist2, 12))

def gettwosum2(arr, number):
    arr.sort()
    result = []
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == number:
            result.append(arr[left])
            result.append(arr[right])
            return result
        if current_sum < number:
            left += 1
        else:
            right -= 1
    return None

print(gettwosum2(alist3,12))



def gettwosum3(arr, number):
    result = []
    previous = set()
    for A in arr:
        Y = number - A
        if Y in previous:
            result.append(Y)
            result.append(A)
            return result
        else:
            previous.add(A)
    return None

print(gettwosum3(alist3,12))
