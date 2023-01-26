#괄호

N = int(input())


for i in range(N):
    a = 0
    b = 0
    temp = input()
    for t in temp:
        if t =='(':
            a += 1
        elif t == ")":
            b += 1
    if a - b == 0:
        print("YES")
    else:
        print("NO")