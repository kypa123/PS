def solution(babbling):
    answer = 0
    for bb in babbling:
        if len(bb) < 2:
            continue
        word = bb
        temp = ''
        while word:
            if word[:3] == 'aya' or word[:3] == 'woo':
                if word[:3] != temp:
                    temp = word[:3]
                    word = word[3:]
                else:
                    break
            elif word[:2] == 'ye' or word[:2] == 'ma':
                if word[:2] != temp:
                    temp = word[:2]
                    word = word[2:]
                else:
                    break
            else:
                break
        if not word:
            answer += 1
    return answer


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))