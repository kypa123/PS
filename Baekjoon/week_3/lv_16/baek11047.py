N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

count = 0

for i in range(1, N+1):
    if arr[-i] <= K:
        curr_count = K // arr[-i]
        count += curr_count
        K -= arr[-i] * curr_count
    if K == 0:
        print(count)
        break
