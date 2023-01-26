from collections import deque
def solution(s):
    q = deque(s)
    answer = True
    stack = []
    while q:
        temp = q.popleft()
        if temp == '(':
            stack.append(temp)
        elif temp == ')' and stack:
            stack.pop()
        else:
            answer = False
            break
    if stack:
        return False
    return answer