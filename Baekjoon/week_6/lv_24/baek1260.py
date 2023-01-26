from collections import deque

N, M, V = map(int, input().split())


def bfs(node):
    que = deque()
    que.append(node)
    visit_list2[node] = 1
    while que:
        node = que.popleft()
        print(node, end = " ")
        for i in range(1, N+1):
            if visit_list2[i] == 0 and arr[node][i] == 1:
                que.append(i)
                visit_list2[i] = 1


def dfs(node):
    visit_list[node] = 1
    print(node, end=" ")
    for i in range(1, N+1):
        if visit_list[i] == 0 and arr[node][i] == 1:
            dfs(i)


arr = [[0] * (N + 1) for _ in range(N + 1)]
visit_list = [0] * (N + 1)
visit_list2 = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

dfs(V)
print()
bfs(V)