from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    print(visited)
    def bfs(i):
        q = deque([i])
        while q:
            i = q.popleft()
            print(i)
            visited[i] = 1
            for z in range(n):
                if computers[i][z] and not visited[z]:
                    q.append(z)

    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer





solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])