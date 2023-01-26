n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
answerarr = []


def calcdiff(curr):
    anotherteam = list(set(range(n)) - set(curr))
    team1 = 0
    team2 = 0
    for k in range(n//2):
        for o in range(k+1, n//2):
            team1 += arr[curr[k]][curr[o]] + arr[curr[o]][curr[k]]
            team2 += arr[anotherteam[k]][anotherteam[o]] + arr[anotherteam[o]][anotherteam[k]]
    diff = abs(team1 - team2)
    if diff == 0:
        print(0)
        exit()
    answerarr.append(diff)


def dfs(curr, l):
    if l == n//2:
        calcdiff(curr)
        return
    for j in range(curr[-1]+1 if curr else 0, n):
        if curr and curr[0] != 0:
            return
        curr.append(j)
        dfs(curr, l+1)
        curr.pop()


for i in range(n):
    dfs([i], 1)

print(min(answerarr))