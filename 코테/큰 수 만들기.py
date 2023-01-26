def solution(number, k):
    answer = []
    # 1231234
    for i in number:
        if not answer:
            answer.append(i)
            print(f'현재: {answer}')
            continue
        while answer[-1] < i and k > 0:
            print(f'{k} 카운트만큼 남아있고 {answer[-1]}이 현재 수 {i}보다 작아요')
            answer.pop()
            print(f'따라서, 현재 {answer} 입니다')
            k -= 1
            print(f'현재 카운트수는 {k}')
            if not answer or k <= 0:
                break
        answer.append(i)
        print(answer)
        if len(answer) == len(number) - k:
            break
    return ''.join(answer)

print(solution('4177252841', 4))