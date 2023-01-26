from itertools import combinations

n, m = map(int,input().split())

arr = [i for i in range(1, n+1)]

c = list(combinations(arr, m))

for cc in c:
    print(*cc)