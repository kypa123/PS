A, B = map(int, (input().split()))
sol = []
arr = list(map(int, input().split()))
for val in arr:
    if val < B:
        sol.append(val)
print(' '.join(map(str, sol)))