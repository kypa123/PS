from collections import deque

N = int(input())

arr = [[]for _ in range(N+1)]

for i in range(N):
    c = list(map(int, input().split()))
    for e in range(1, len(c) - 2, 2):
        arr[c[0]].append((c[e], c[e + 1]))


def bfs(node):
    visit = [0] * (N+1)
    que = deque()
    que.append(node)
    visit[node] = 0
    sol = [0, 0]

    while que:
        temp = que.popleft()
        for x, y in arr[temp]:
            if visit[x] == 0:
                visit[x] = visit[temp] + y
                que.append(x)
                if sol[0] < visit[x]:
                    sol = visit[x], x

    return sol


ans, node = bfs(1)
ans, node = bfs(node)

print(ans)