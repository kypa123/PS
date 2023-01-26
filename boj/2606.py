global array
global visited
n = int(input())
m = int(input())
array = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    array[a].append(b)
    array[b].append(a)


visited = [False] * (n + 1)
count = 0


def dfs(v):
    global count
    visited[v] = True
    for val in array[v]:
        if not visited[val]:
            count += 1
            dfs(val)


dfs(1)

print(count)