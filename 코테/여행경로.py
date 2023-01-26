def solution(tickets):
    answer = []
    target = len(tickets)

    def dfs(curr, visit, cnt):
        for j in range(target):
            print(f'{cnt}, 현재값은 {tickets[j]}')
            if visit[j] != 1 and tickets[j][0] == curr[-1]:
                print(f'{cnt}, {curr}, {tickets[j]}{visit}')
                curr.append(tickets[j][1])
                visit[j] = 1
                print(f'성공했으니까 {curr}, {visit}')
                dfs(curr, visit, cnt+1)
                visit[j] = 0
            elif visited[j] == 1:
                print(f'{tickets[j]}는 이미 방문했습니다. {curr}, {visited}')
            else:
                print(f'{tickets[j]}는 {curr}의 끝자리와 맞지않네요.')

    for i in range(target):
        visited = [0] * len(tickets)
        visited[i] = 1
        temp = [tickets[i][0], tickets[i][1]]
        dfs(temp, visited, 1)
    answer.sort()
    return answer[0]


print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))

ans = [0]
def dfs(pos, path):
    # base case
    if len(path) == 5:
        ans[0] += 1
        return

    # loop
    for next_pos in range():

        path.append()
        dfs(next_pos, path + [item])
        path.pop()
