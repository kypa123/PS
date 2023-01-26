from collections import Counter

def solution(topping):
    answer = 0
    s = set()
    c = Counter(topping)
    for t in topping:
        s.add(t)
        c[t] -= 1
        if c[t] == 0:
            del c[t]
        if len(s) == len(c):
            answer += 1
    return answer


print(solution([1,2,1,3,1,4,1,2]))