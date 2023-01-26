def solution(arrayA, arrayB):
    answer = [0]
    a1 = []
    a2 = []
    for i in range(2, min(arrayA)+1):
        for a in arrayA:
            if a % i == 0:
                continue
            break
        else:
            a1.append(i)
    for j in range(2, min(arrayB)+1):
        for b in arrayB:
            if b % j == 0:
                continue
            break
        else:
            a2.append(j)
    for n in a1:
        for b in arrayB:
            if b % n != 0:
                continue
            break
        else:
            answer.append(n)
    for m in a2:
        for a in arrayB:
            if a % m != 0:
                continue
            break
        else:
            answer.append(m)
    return max(answer)

print(solution([10, 20],[5, 17]))