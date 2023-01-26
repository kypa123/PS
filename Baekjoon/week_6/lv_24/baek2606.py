N = int(input())
connect = int(input())

arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(connect):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

count = 0


def dfs(node):
    global count
    visited[node] = 1
    for val in arr[node]:
        if visited[val] == 0:
            dfs(val)
            count += 1


dfs(1)
print(count)