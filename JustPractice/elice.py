from collections import deque

# def findSurvivor(total):
#     q1 = deque()
#     for people in range(total):
#         q1.append(people + 1)
#
#     while len(q1) > 1:
#         q1.append(q1.popleft())
#         q1.popleft()
#
#     return q1.popleft()
#
# ans = findSurvivor(100)
#
# print(ans)