from collections import deque


def solution(board, moves):
    answer = 0
    arr = []
    for i in range(len(board)):
        q = deque()
        for j in range(len(board)):
            if board[j][i] != 0:
                q.append(board[j][i])
        arr.append(q)

    curr = []
    for move in moves:
        if arr[move-1]:
            curr.append(arr[move - 1].popleft())


    temp = 0
    limit = len(curr)
    while temp < limit-1:
        if curr[temp] == curr[temp+1]:
            answer += 2
            curr.pop(temp)
            curr.pop(temp)
            temp = 0
            limit -= 2
            continue
        temp += 1
    return answer


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])