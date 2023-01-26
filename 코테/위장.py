def solution(clothes):
    d = dict()
    for key, val in clothes:
        d[val] = d.get(val, 0) + 1

    answer = 1
    for val in d:
        answer *= (d[val] + 1)

    return answer - 1