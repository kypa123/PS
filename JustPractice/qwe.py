def solution(a, b, n):
    answer = 0
    while n >= a:
        curr = n // a
        left = n % a
        answer += curr * b
        n = left + curr * b

    return answer