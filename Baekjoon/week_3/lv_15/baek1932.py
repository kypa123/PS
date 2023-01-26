N = int(input())
arr = [list(map(int, (input().split())))for i in range(N)]

for i in range(N-1, -1, -1):
    if i == N-1:
        continue
    for j in range(len(arr[i])):
        arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])


print(arr[0][0])

#아래에서부터 가장 큰 숫자의 합으로 올라감.