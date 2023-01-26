def getMaxBarrier(initialEnergy, th):
    maximum = max(initialEnergy)
    initialEnergy.sort()
    total = 0
    curr = 1
    cnt = 0
    flag = True
    while True:
        if not flag:
            break
        temp = initialEnergy.pop()
        if initialEnergy:
            temp -= initialEnergy[-1]
        else:
            break
        for i in range(temp):
            total += curr
            cnt += 1
            if total >= th:
                flag = False
                break
        curr += 1
    return maximum - cnt
print(getMaxBarrier([5,2,13,10],8))