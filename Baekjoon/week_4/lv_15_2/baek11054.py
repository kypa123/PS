N = int(input())
arr = list(map(int ,input().split()))
dp_inc = [1 for i in range(N)]
dp_dec = [1 for i in range(N)]
sol = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[i] > arr[j]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)

for i in range(N):
    sol[i] = dp_inc[i] + dp_dec[i] - 1

print(max(sol))
