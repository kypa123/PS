class Solution:
    def generateParenthesis(self, n):
        def bt(s, left, right, result):
            if left:
                bt(s+'(', left-1, right, result)
            if right>left:
                bt(s+')', left, right-1, result)
            if not right:
                result.append(s)
            return result
        return bt('', n, n, [])


S = Solution()
print(S.generateParenthesis(3))