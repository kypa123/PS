from collections import Counter


def solution(gems):
    count = len(Counter(gems))
    start = 0
    end = len(gems)
    answer = []

    while start < end:
        if len(Counter(gems[start:end-1])) == count:
            end -= 1
        elif len(Counter(gems[start + 1:end])) == count:
            start += 1
        else:
            answer.append(start + 1)
            answer.append(end)
            break

    return answer
