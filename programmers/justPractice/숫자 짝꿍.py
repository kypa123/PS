from collections import defaultdict


def solution(X, Y):
    answer = ''
    x = defaultdict(int)
    y = defaultdict(int)
    for n in X:
        x[n] += 1
    for m in Y:
        y[m] += 1
    for key, val in x.items():
        if y[key]:
            answer += key * min(val, y[key])

    if answer:
        if int(answer) == 0:
            return '0'
        else:
            return answer
    return -1

print(solution('12321','42531'))