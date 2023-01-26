import sys

N = int(sys.stdin.readline())
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr = [[0 for _ in range(b+1)] for _ in range(a+1)]
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if i == 1:
                arr[i][j] = j
                continue
            if i == j:
                arr[i][j] = 1
            else:
                if j > i:
                    arr[i][j] = arr[i][j-1] + arr[i-1][j-1]
    print(arr[i][j])