def draw_star(n):
    if n == 3:
        arr[0][:3] = arr[2][:3] = ["*"]*3
        arr[1][:3] = ["*", " ", "*"]
        return
    a = n//3
    draw_star(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                arr[a*i+k][a*j:a*(j+1)] = arr[k][:a]


N = int(input())

arr = [[" " for i in range(N)]for i in range(N)]

draw_star(N)

for val in arr:
    print("".join(val))