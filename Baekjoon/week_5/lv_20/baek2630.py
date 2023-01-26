def solution(x, y, n: int):
    global arr, white, blue
    color = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color:
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1


white = 0
blue = 0

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

solution(0, 0, N)
print(white)
print(blue)
