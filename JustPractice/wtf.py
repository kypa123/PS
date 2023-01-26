from itertools import combinations
class Solution:
    def subsets(self, nums):
        sol = []
        for i in range(len(nums)+1):
            c = list(combinations(nums, i))
            for z in c:
                sol.append(list(z))
        return sol

S = Solution()
S.subsets([1,2,3])