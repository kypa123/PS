def solution(board):
    visited = [[False] * len(board[0]) for _ in range(len(board))]
    danger = [[0] * len(board[0]) for _ in range(len(board))]
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1 and not visited[i][j]:
                danger[i][j] = 1
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < len(board) and 0 <= y < len(board):
                        danger[x][y] = 1
            visited[i][j] = True
    answer = len(board) * len(board)
    for d in danger:
        print(sum(d))
        answer -= sum(d)
    return answer



print(solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]))