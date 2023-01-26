from collections import deque

y, x = map(int, input().split()) # 4, 6
arr = [list(map(int, input().split())) for _ in range(x)]

visited = []
answer = 0
q = deque()

nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]


for i in range(x):
    for j in range(y):
        if not isPossible(i, j) and arr[i][j] != -1:
            print(-1)
            exit(0)
        if arr[i][j] == 1:
            q.append((0, i, j))
            visited.append((i,j))

while q:
    day, a, b = q.popleft()
    for i in range(4):
        dx = a + nx[i]
        dy = b + ny[i]
        if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]) and arr[dx][dy] != -1 and (dx,dy) not in visited:
            q.append((day + 1, dx, dy))
            answer = max(day + 1, answer)
            visited.append((dx,dy))
            arr[dx][dy] = 1

if answer == 0:
    print(-1)
else:
    print(answer)
