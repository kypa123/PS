N, K = map(int, (input().split()));

arr = []
for i in range(N):
    arr.append(int(input()))

count = 0

for j in range(1, N+1):
    if arr[-j] <= K:
        minus = K // arr[-j]
        count += minus
        K = K % arr[-j]
    if K == 0:
        print(count)
        break