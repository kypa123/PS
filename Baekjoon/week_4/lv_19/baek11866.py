N, X = map(int, (input().split()))

arr = [i for i in range(1, N + 1)]
sol = []
temp = X - 1
print("<", end="")
while arr:
    if len(arr) == 1:
        print(arr[0], end="")
        break
    if len(arr) > temp:
        print(arr.pop(temp), end=", ")
        temp += X - 1
    else:
        temp -= len(arr)
print(">", end="")
