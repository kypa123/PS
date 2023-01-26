import sys
N = int(sys.stdin.readline())

for _ in range(N):
    count = 0
    temp = input()
    for i in temp:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            print("NO")
            break
    if count == 0:
        print("YES")
    elif count > 0:
        print("NO")
