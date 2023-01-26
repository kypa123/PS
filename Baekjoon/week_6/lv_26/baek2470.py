N = int(input())
arr = sorted(list(map(int, input().split())))

a = 0
b = N-1
ans = 2e+9+1

sol = []

while a < b:
    temp = arr[a] + arr[b]
    if abs(temp) < ans:
        ans = abs(temp)
        sol = [arr[a], arr[b]]
        if ans == 0:
            break
    if temp < 0:
        a += 1
    else:
        b -= 1


print(sol[0], sol[1])