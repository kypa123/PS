N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]

ans = []


def sol(x, y, n: int):
    global arr, ans
    number = arr[x][y]
    flag = False
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != number:
                flag = True
                break

    if flag:
        sol(x, y, n // 3)
        sol(x + n // 3, y, n // 3)
        sol(x + n * 2 // 3, y, n // 3)
        sol(x, y + n // 3, n // 3)
        sol(x + n // 3, y + n // 3, n // 3)
        sol(x + n * 2 // 3, y + n // 3, n // 3)
        sol(x, y + n * 2 // 3, n // 3)
        sol(x + n // 3, y + n * 2 // 3, n // 3)
        sol(x + n * 2 // 3, y + n * 2 // 3, n // 3)

    else:
        ans.append(number)


sol(0, 0, N)

print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))