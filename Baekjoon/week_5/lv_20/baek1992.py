N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


def solution(x, y, n):
    number = arr[x][y]
    flag = False
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != number:
                flag = True
                break

    if flag:
        print("(", end='')
        n = n // 2
        solution(x, y, n)
        solution(x, y + n, n)
        solution(x + n, y, n)
        solution(x + n, y + n, n)
        print(")", end='')

    else:
        print(number, end='')


solution(0, 0, N)

