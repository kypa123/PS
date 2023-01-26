N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())

arr.sort(key=lambda x: int(x[0]))

for val in arr:
    print(val[0], val[1])