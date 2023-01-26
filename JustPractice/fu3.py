def solution(scores):
    answer = 0
    scores.sort(key=lambda x:x[0])
    print(scores)
    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))

