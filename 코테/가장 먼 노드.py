from collections import deque


def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n + 1)]
    distance = [-1] * (n + 1)

    for e in edge:
        arr[e[0]].append(e[1])
        arr[e[1]].append(e[0])

    q = deque([1])
    distance[1] = 0
    while q:
        temp = q.popleft()

        for i in arr[temp]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[temp] + 1

    for d in distance:
        if d == max(distance):
            answer += 1

    return answer
