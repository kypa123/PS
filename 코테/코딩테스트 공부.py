from collections import deque


def solution(alp, cop, problems):
    arr = []
    target1 = target2 = 0
    for problem in problems:
        target1 = max(target1, problem[0])
        target2 = max(target2, problem[1])
    print(target1, target2)
    q = deque([(alp, cop, 0)])

    while q:
        alpw, copw, count = q.popleft()
        print(alpw,copw, count)
        if alpw >= target1 and copw >= target2:
            arr.append((alpw, copw, count))
            continue
        else:
            if alpw < target1:
                q.append((alpw + 1, copw, count +1))
            if copw < target2:
                q.append((alpw, copw+1, count + 1))
            for problem in problems:
                if alpw >= problem[0] and copw >= problem[1] and ((alpw < target1 and problem[2] > 0) or (copw < target2 and problem[3] > 0)):
                    q.append((alpw + problem[2], copw + problem[3], count + problem[4]))
    print(arr)
    answer = 0
    return answer


print(solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]]))