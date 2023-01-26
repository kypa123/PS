from itertools import combinations
import math

def solution(nums):
    answer = 0

    def isPrime(number):
        if number == 1:
            return False
        for i in range(2, int(math.sqrt(number)+1)):
            if number % i == 0:
                return False
        return True

    comb = list(combinations(nums, 3))
    for c in comb:
        if isPrime(sum(c)):
            answer += 1

    return answer
