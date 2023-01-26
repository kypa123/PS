from collections import Counter
def solution(nums):
    c = Counter(nums)
    limit = len(nums) // 2
    if len(c) > limit:
        return limit
    else:
        return len(c)


