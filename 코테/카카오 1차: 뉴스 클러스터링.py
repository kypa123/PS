from collections import defaultdict


def solution(str1, str2):
    sameword = 0
    d1 = defaultdict(int)
    d2 = defaultdict(int)

    str1, str2 = str1.lower(), str2.lower()
    for i in range(len(str1) - 1):
        temp1, temp2 = str1[i], str1[i + 1]
        if 97 <= ord(temp1) <= 122 and 97 <= ord(temp2) <= 122:
            d1[temp1 + temp2] += 1

    for i in range(len(str2) - 1):
        temp1, temp2 = str2[i], str2[i + 1]
        if 97 <= ord(temp1) <= 122 and 97 <= ord(temp2) <= 122:
            d2[temp1 + temp2] += 1
    for word in d1:
        if word in d2:
            sameword += min(d1[word], d2[word])
            d2[word] = max(d1[word], d2[word])
        else:
            d2[word] = d1[word]

    alllen = 0
    for word in d2:
        alllen += d2[word]
    if sameword == alllen == 0:
        return 65536
    else:
        answer = int((sameword / alllen) * 65536)
    return answer