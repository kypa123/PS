def solution(food):
    temp = ''
    answer = ''
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            temp += str(i)
    temp += '0'
    answer += temp
    for k in range(len(temp) - 2, -1, -1):
        answer += temp[k]

    return answer