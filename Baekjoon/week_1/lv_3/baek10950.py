N = int(input())
sol = []
for i in range(N):
    A, B = map(int, input().split())
    sol.append(A+B)
for ans in sol:
    print(ans)