N = int(input())

def sol(x) :
    if x in (1,2):
        return x
    elif x==3:
        return 4
    else:
        return sol(x-1) + sol(x-2) + sol(x-3)

for i in range(N) :
    x = int(input())
    print(sol(x))