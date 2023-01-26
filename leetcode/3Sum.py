def threeSum(nums):
    nums.sort()
    N, result = len(nums), []
    for i in range(N):
        target = nums[i]*-1
        s,e = i+1, N-1
        while s<e:
            if nums[s]+nums[e] == target:
                if [nums[i], nums[s], nums[e]] not in result:
                    result.append([nums[i], nums[s], nums[e]])
                s = s+1
                while s<e and nums[s] == nums[s-1]:
                    s = s+1
            elif nums[s] + nums[e] < target:
                s = s+1
            else:
                e = e-1
    return result

print(threeSum([-1,0,1,2,-1,-4]))

# 4790 / 18