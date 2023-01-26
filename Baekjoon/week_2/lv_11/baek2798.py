N, M = map(int, input().split())

arr = list(map(int, input().split()))

arr2 = []
ans = 0
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            arr2.append(arr[i]+arr[j]+arr[k])

for val in arr2:
    if val > M:
        continue
    if val == M:
        ans = val
        break
    elif ans < val <= M:
        ans = val
print(ans)
