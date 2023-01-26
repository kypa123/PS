def solution(triangle):
    for i in range(1, len(triangle)):
        answer = 0
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    answer = max(triangle[-1])
    return answer
