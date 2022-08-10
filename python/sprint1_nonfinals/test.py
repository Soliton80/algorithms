A = [10, 10, 23, 10, 123, 66, 78, 123]
counter = {}

for elem in A:
    counter[elem] = counter.get(elem, 0) + 1

doubles = {element: count for element, count in counter.items() if count > 1}

print(counter)
print(doubles)