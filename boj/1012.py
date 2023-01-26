from collections import deque

solution = []
num = int(input())

def bfs(x,y):
    answer = 0
    nx = [-1,1,0,0]
    ny = [0,0,-1,1]
    q = deque()
    q.append((x,y))
    while q:
        a, b = q.popleft()
        for l in range(4):
            dx = a + nx[l]
            dy = b + ny[l]
            if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]) and arr[dx][dy] == 1 and (dx,dy) not in visited:
                visited.append((dx,dy))
                q.append((dx,dy))

for i in range(num):
    answer = 0
    m, n, count = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = []
    for j in range(count):
        y, x = map(int, input().split())
        arr[x][y] = 1

    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1 and (r, c) not in visited:
                answer += 1
                visited.append((r, c))
                bfs(r, c)
    solution.append(answer)

for s in solution:
    print(s)