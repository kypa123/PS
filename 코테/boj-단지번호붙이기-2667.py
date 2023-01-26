from collections import deque

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input())))

global dx
global dy
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# def bfs(x,y):
#     q = deque()
#     q.append((x, y))
#     arr[x][y] = 0
#     count = 1
#
#     while q:
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if arr[nx][ny] == 1:
#                 arr[nx][ny] = 0
#                 q.append((nx, ny))
#                 count += 1
#     return count
#
#
# sol = []
# for z in range(n):
#     for c in range(n):
#         if arr[z][c] == 1:
#             sol.append(bfs(z,c))
#
# print((len(sol)))
# sol.sort()
# for s in sol:
#     print(s)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if arr[x][y] == 1:
        global count
        count += 1
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


count = 0
sol = []

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            sol.append(count)
            count = 0

sol.sort()
print(len(sol))
for s in sol:
    print(s)