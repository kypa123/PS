#스택

N = int(input())
arr = []
for i in range(N):
    arr.append(input().split())


sol = []
for val in arr:
    if val[0] == 'push':
        sol.append(val[1])
    elif val[0] == 'pop':
        if len(sol) == 0:
            print(-1)
        else:
            print(sol.pop(-1))
    elif val[0] == 'size':
        print(len(sol))
    elif val[0] == 'empty':
        if len(sol) == 0:
            print(1)
        else:
            print(0)
    elif val[0] == 'top':
        if len(sol) == 0:
            print(-1)
        else:
            print(sol[-1])