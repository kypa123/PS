N = int(input())

sol = [0] * 10000000

for i in range(2, N+1):
    sol[i] = sol[i-1]+1

    if i % 2 == 0:
        sol[i] = min(sol[i], sol[i//2] + 1)

    if i % 3 == 0:
        sol[i] = min(sol[i], sol[i // 3] + 1)

print(sol[N])


#1로만들기 유형의 교과서.