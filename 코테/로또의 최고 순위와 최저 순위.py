def solution(lottos, win_nums):
    lottos.sort()
    best = 0
    worst = 0
    while lottos:
        temp = lottos.pop()
        if temp in win_nums:
            best += 1
            worst += 1
            win_nums.remove(temp)
        if temp == 0:
            best += 1
    best = 6 if 7 - best >= 6 else 7 - best
    worst = 6 if 7 - worst >= 6 else 7 - worst
    answer = [best, worst]
    return answer