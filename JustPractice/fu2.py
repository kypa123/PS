from collections import deque

def solution(r, delivery):
    arr = []
    mx = [-1,1,0,0]
    my = [0,0,-1,1]

    q = deque()

    q.append((0,0,0,0,[(0,0)]))

    matrix = []
    l = r*r
    for i in range(0, r*r, r):
        matrix.append(delivery[i:i+r])

    while q:
        x,y,total,cnt,visited = q.popleft()
        if len(visited) == l:
            arr.append(total)
            continue
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0 <= nx < r and 0 <= ny < r:
                if (nx, ny) not in visited:
                    visited.append((nx, ny))
                    if matrix[nx][ny][0] >= cnt:
                        total += matrix[nx][ny][1]
                q.append((nx, ny, total, cnt+1, visited))
        if cnt == r*r:
            arr.append(total)
        print(x,y,total,cnt,visited)

    return max(arr)


print(solution(3,[[1,5],[8,3],[4,2],[2,3],[3,1],[3,2],[4,2],[5,2],[4,1]]))