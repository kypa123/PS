import sys
N = int(input())
sys.setrecursionlimit(10**6)

arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(node):
    for i in arr[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)


dfs(1)


for x in range(2, N+1):
    print(visited[x])
