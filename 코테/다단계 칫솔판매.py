from collections import defaultdict


def solution(enroll, referral, seller, amount):
    connection = defaultdict()
    for i in range(len(enroll)):
        connection[enroll[i]] = referral[i]
    answer = defaultdict(int)
    for j in range(len(seller)):
        surplus = amount[j] * 10
        if surplus < 1:
            answer[seller[j]] = amount[j] * 100
            continue
        mine = amount[j] * 90
        answer[seller[j]] += mine
        temp = connection[seller[j]]
        while True:
            if temp == '-':
                break
            ttemp = surplus // 10
            answer[temp] += surplus - ttemp
            surplus = ttemp
            if surplus == 0:
                break
            temp = connection[temp]
    sol = []
    for k in range(len(enroll)):
        sol.append(answer[enroll[k]])
    return sol

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])