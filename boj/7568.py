N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

for j in range(N):
    count = 1
    temp = arr[j]
    for k in range(N):
        if arr[k][0] > arr[j][0] and arr[k][1] > arr[j][1]:
            count += 1
    print(count)