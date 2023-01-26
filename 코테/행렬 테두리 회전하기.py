from collections import deque
def solution(rows, columns, queries):
    arr = []
    answer = []
    for i in range(1, rows + 1):
        temp = columns * i
        temparr = []
        for j in range(temp - columns + 1, temp + 1):
            temparr.append(j)
        arr.append(temparr)

    for query in queries:
        temp = deque()
        col, row = query[2] - query[0] + 1, query[3] - query[1] + 1
        for i in range(row):
            temp.append(arr[query[0]-1][query[1]+i-1])
        for i in range(col-1):
            temp.append(arr[query[0]+i][query[3]-1])
        for i in range(row-1):
            temp.append(arr[query[2]-1][query[3]-i-2])
        for i in range(col-2):
            temp.append(arr[query[2]-i-2][query[1]-1])
        answer.append(min(temp))
        for i in range(row):
            if i == 0:
                curr = temp.pop()
            else:
                curr = temp.popleft()
            arr[query[0] - 1][query[1] + i - 1] = curr
        for i in range(col - 1):
            curr = temp.popleft()
            arr[query[0] + i][query[3] - 1] = curr
        for i in range(row - 1):
            curr = temp.popleft()
            arr[query[2] - 1][query[3] - i - 2] = curr
        for i in range(col - 2):
            curr = temp.popleft()
            arr[query[2] - i - 2][query[1] - 1] = curr
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))