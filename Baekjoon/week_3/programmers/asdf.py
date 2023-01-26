arr = [i for i in range(14)]
for i in range(12):
    if i == 0:
        arr.append(12)
        continue
    arr.append(arr[-1]-1)


print(arr)