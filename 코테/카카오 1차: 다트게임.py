from collections import deque


def solution(dartResult):
    q = deque(dartResult)
    arr = [0] * (len(dartResult) + 2)
    curr = 2
    while q:
        word = q.popleft()
        if word == '*':
            arr[curr-1] *= 2
            arr[curr-2] *= 2
            continue
        elif word == '#':
            arr[curr-1] *= -1
            continue
        else:
            if q:
                bonus = ''
                next = q.popleft()
                if next == '0':
                    bonus = q.popleft()
                    word = '10'
                else:
                    bonus = next
                if bonus == 'S':
                    arr[curr] = int(word)
                elif bonus == 'D':
                    arr[curr] = int(word) ** 2
                else:
                    arr[curr] = int(word) ** 3
            curr += 1
    return sum(arr)