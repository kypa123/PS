from collections import deque

def solution(map):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    q = deque()
    q.append([0,0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx < len(map) and 0 <= yy < len(map[0]) and map[xx][yy] == 1:
                map[xx][yy] = map[x][y] + 1
                q.append((xx, yy))
    return -1 if map[len(map)-1][len(map[0])-1] == 1 else map[len(map)-1][len(map[0])-1]


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))