def solution(msg):
    answer = []
    alphabet = dict()
    for i in range(1, 27):
        alphabet[chr(i + 64)] = i
    temp = ''
    lastnum = 27
    for j in range(len(msg)):
        temp += msg[j]
        if temp not in alphabet:
            alphabet[temp] = lastnum
            lastnum += 1
            while True:
                temp = temp[:-1]
                if temp in alphabet:
                    answer.append(alphabet[temp])
                    break
            temp = msg[j]
    print(answer)
    return answer

solution('KAKAO')