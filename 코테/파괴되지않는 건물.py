def solution(board, skill):
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, a, b, c, d, degree in skill:
        if t == 2:
            degree = -degree
        temp[a][b] -= degree
        temp[a][d+1] += degree
        temp[c+1][b] += degree
        temp[c+1][d+1] -= degree
    for i in range(len(temp) - 1):
        for j in range(len(temp[0])-1):
            temp[i][j+1] += temp[i][j]
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i+1][j] += temp[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + temp[i][j] > 0:
                answer += 1
    return answer


# solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])