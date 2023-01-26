def solution(babbling):
    answer = 0
    word = ['aya', 'ye', 'woo', 'ma']
    banword = ['ayaaya','yeye','woowoo','mama']
    for b in babbling:
        print(f'{b} 시작')
        while True:
            if b in banword:
                break
            elif b in word:
                print(b)
                answer += 1
                break
            elif b[:3] in word:
                b = b[3:]
                print(f'3개단위로 찾음.{b}')
                continue
            elif b[:2] in word:
                b = b[2:]
                print(f'2개단위로 찾음 {b}')
                continue
            else:
                break
    return answer

print(solution(["ayaayaye"]))