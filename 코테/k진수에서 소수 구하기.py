def calc(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return ''.join(reversed(rev_base))

def isPrime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    temp = calc(n, k)
    for num in temp.split("0"):
        if num == "":
            continue
        if isPrime(int(num)):
            answer += 1
    return answer
