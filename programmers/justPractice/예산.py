def solution(d, budget):
    d.sort()
    curr = 0
    for i, v in enumerate(d):
        curr += v 
        print(curr)
        if curr > budget:
            return i
        elif curr == budget:
            return i+1
        elif i + 1 == len(d):
            return i + 1

print(solution([100],101))