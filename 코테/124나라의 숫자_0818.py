def solution(n):
    nation = [4, 1, 2]
    li = []
    if n > 0:
        temp = n
        while temp // 3 > 0:
            if temp % 3 == 0:
                li.append(temp % 3)
                temp = temp - 1
            else:
                li.append(temp % 3)
            temp = temp // 3
        if temp != 0:
            li.append(temp)


    answer = []
    for i in li[::-1]:
        if i == 0:
            answer.append(str(nation[i]))
        elif i == 1:
            answer.append(str(nation[i]))
        elif i == 2:
            answer.append(str(nation[i]))

    return ''.join(answer)