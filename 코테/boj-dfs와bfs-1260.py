from collections import deque
a, b, c = map(int, input().split())

global array
global visited

array = [[] for i in range(a + 1)]

for i in range(b):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)
print(array)
for arr in array:
    arr.sort()

visited = [False] * (a + 1)


def dfs(v):
    visited[v - 1] = True
    print(v, end=' ')
    for value in array[v]:
        if not visited[value - 1]:
            dfs(value)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        value = q.popleft()
        print(value, end=' ')
        for i in array[value]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(c)
visited = [False] * (a + 1)
print()
bfs(c)