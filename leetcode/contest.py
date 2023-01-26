from collections import deque


def countSubarrays(nums, k):
    l = len(nums)
    answer = 1
    idx = nums.index(k)
    left = idx
    right = idx
    q = deque()
    q.append((left, right, 0))

    lvalue = rvalue = 0
    while q:
        lft, rgt, checker = q.popleft()
        if lft - 1 >= 0:
            lvalue = nums[lft -1]
        if rgt + 1 < l:
            rvalue = nums[rgt + 1]

        if checker == 0:
            if lvalue >= k:
                print(lvalue, checker + 1)
                q.append((lft - 1, rgt, 1))
                answer += 1
            if rvalue >= k:
                print(rvalue, checker + 1)
                q.append((lft, rgt + 1, 1))
                answer += 1
        elif checker == 1:
            if rvalue <= k:
                print(rvalue, checker -1)
                q.append((lft, rgt + 1, 0))
                answer += 1
            if lvalue <= k:
                print(lvalue, checker -1)
                q.append((lft - 1, rgt, 0))
                answer += 1
        print(lft, rgt, checker)
    return answer

print(countSubarrays([3,2,1,4,5], 4))