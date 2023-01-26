N = input()
arr = []
for i in N:
    arr.append(int(i))


arr.sort(reverse=True)
for val in arr:
    print(val, end='')