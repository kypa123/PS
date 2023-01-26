from collections import deque


def check(word):
    stack = []
    for w in word:
        if stack:
            if stack[-1] == '(' and w == ')':
                stack.pop()
            else:
                stack.append(w)
        else:
            if w == ')':
                return False
            stack.append(w)
    if stack:
        return False
    return True


def balanceCheck(word):
    stack = [word[0]]
    for i in range(1, len(word)):
        if word[i] != stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])
        if not stack:
            return i
    return 0


def solution(p):
    answer = ''
    if p == '':
        return answer
    if check(p):
        return p

    result = balanceCheck(p)
    while True:
        u, v = p[:result+1], p[result+1:]
        print(u)
        print(v)
        if check(u):
            answer += u
            result = balanceCheck(v)
            continue
        else:
            temp = '('
            if u:
                curr = u[1:-1]
                for c in curr:
                    if c == '(':
                        temp += ')'
                    elif c == ')':
                        temp += '('
                    else:
                        break
            temp += ')'
            temp += v
    return answer


print(solution("()))((()"))