class Solution:
    def bt(self, digits, ans, letter, word, idx):
        if len(digits) == idx:
            print(f'word:{word}, {ans}에 합칩니다.')
            ans.append(word)
            return
        for l in letter[int(digits[idx])]:
            print(f'재귀입니다. 현재 모인 값은 :{ans}, 현재단어는: {word},여기에 {l}을 합쳐 {word + l}. idx:{idx}')
            self.bt(digits, ans, letter, word + l, idx + 1)

    def letterCombinations(self, digits):
        ans = []
        if len(digits) == 0:
            return ans
        letter = ["", "",['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'],
              ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        self.bt(digits, ans, letter, "", 0)
        return ans


S = Solution()
print(S.letterCombinations("23"))