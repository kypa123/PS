from collections import defaultdict


def solution(survey, choices):
    answer = ''
    character = [["R", "T"], ["C","F"], ["J", "M"], ["A", "N"]]
    d = defaultdict(int)
    for i in range(len(survey)):
        c = choices[i]
        if c < 4:
            d[survey[i][0]] += 4 - c
        elif c > 4:
            d[survey[i][1]] += c - 4

    for j in range(4):
        temp1, temp2 = character[j][0], character[j][1]
        if d[temp1] >= d[temp2]:
            answer += temp1
        elif d[temp1] < d[temp2]:
            answer += temp2
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))