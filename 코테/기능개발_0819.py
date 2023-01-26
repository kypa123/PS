import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    q = deque()
    for x, y in zip(progresses, speeds):
        q.append(math.ceil((100 - x) / y))
    count = 1
    biggest = 0
    while q:
        temp = q.popleft()
        if temp > biggest:
            biggest = temp
        if q:
            if biggest >= q[0]:
                count += 1
            else:
                answer.append(count)
                count = 1
                biggest = 0
        else:
            answer.append(count)
    return answer
