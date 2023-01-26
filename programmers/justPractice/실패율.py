from collections import defaultdict, Counter

def solution(N, stages):
    temp = []
    answer = []
    d = defaultdict(int)
    c = Counter(stages)
    for s in stages:
        for i in range(1, s+1):
            d[i] += 1

    for j in range(1,N+1):
        if not c[j]:
            temp.append((j, 0))
        else:
            temp.append((j, c[j]/d[j]))
    temp.sort(key=lambda x:x[1], reverse=True)
    for t in temp:
        answer.append(t[0])
    return answer


print(solution(4,[4,4,4,4,4]))