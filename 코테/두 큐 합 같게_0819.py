from collections import deque


def solution(queue1, queue2):
    deadline = len(queue1) * 3 + 2
    s1, s2 = sum(queue1), sum(queue2)
    if (s1 + s2) % 2 != 0:
        return -1
    target = (s1 + s2) // 2
    for i, j in zip(queue1, queue2):
        if i > target or j > target:
            return -1

    q1, q2 = deque(queue1), deque(queue2)
    count = 0

    while True:
        if s1 == s2:
            break

        if s1 > s2:
            temp = q1.popleft()
            q2.append(temp)
            s1 -= temp
            s2 += temp
            count += 1
        else:
            temp = q2.popleft()
            q1.append(temp)
            s2 -= temp
            s1 += temp
            count += 1
        if count >= deadline:
            count = -1
            break

    answer = count
    return answer
