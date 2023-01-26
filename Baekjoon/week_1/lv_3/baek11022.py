N = int(input())
count = 1
sol = {}
for i in range(N):
    A, B = input().split()
    key = "Case #" + str(count) + ":"
    sol[key] = A + " + " + B + " = " + str(int(A)+int(B))
    count += 1

for a, b in sol.items():
    print(a, b)