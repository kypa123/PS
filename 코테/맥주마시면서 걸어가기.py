from collections import deque

t = int(input())    #테케 숫자
for _ in range(t):
    n = int(input()) # 편의점 숫자
    home = list(map(int,(input().split()))) #집 위치
    conv = []
    for __ in range(n):
        conv.append(list(map(int, input().split())))    #편의점 위치
    fest = list(map(int, input().split()))
    visited = [False] * (n + 1)
    flag = False
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            flag = True
            break
        for i in range(n):
            if abs(x - conv[i][0]) + abs(y - conv[i][1]) <= 1000 and not visited[i]:
                q.append(conv[i])
                visited[i] = True

    if flag:
        print('happy')
    else:
        print('sad')