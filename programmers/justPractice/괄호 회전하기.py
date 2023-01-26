from collections import deque


def solution(s):
    d = dict()
    d[']'] = '['
    d[')'] = '('
    d['}'] = '{'

    open = ['[', '(', '{']
    close = [']', ')', '}']
    def check(arr):
        stack = []
        for a in arr:
            if stack:
                if a in close and stack[-1] == d[a]:
                    stack.pop()
                else:
                    stack.append(a)
            else:
                if a in close:
                    return False
                stack.append(a)
        if stack:
            return False
        return True

    answer = 0
    q = deque(s)
    for i in range(len(s) - 1):
        if check(q):
            answer += 1
        temp = q.popleft()
        q.append(temp)

    return answer