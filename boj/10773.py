#제로

N =int(input())
arr = []
for i in range(N):
    val = int(input())
    if val == 0:
        arr.pop(-1)
    else:
        arr.append(val)

print(sum(arr))