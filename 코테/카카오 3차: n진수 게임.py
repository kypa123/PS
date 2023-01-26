def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

0, 1, 10, 11, 100, 101, 110, 111
def solution(n, t, m, p):
    temp = p - 1
    answer = ''
    if temp == 0:
        answer = '0'
        temp += m
    while len(answer) <= t:
        answer += str(convert(temp, n))
        print(temp, answer)
        temp += m

    return answer[:t]

print(solution(2,4,2,1))