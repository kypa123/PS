from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    l = len(words)
    wordlen = len(target)
    arr = [0] * l
    q = deque()
    q.append((begin,arr, 0))

    while q:
        temp, temparr, currcount = q.popleft()
        print(temp,temparr)
        if temp == target:
            return currcount

        for i in range(l):
            if temparr[i] == 1:
                continue
            count = 0
            for t in range(wordlen):
                if temp[t] == words[i][t]:
                    count += 1
            if count == wordlen - 1:
                temparr[i] = 1
                q.append((words[i],temparr, currcount + 1))

