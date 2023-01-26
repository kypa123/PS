#문자열 압축
def solution(s):
    sol = len(s)
    for i in range(1, len(s)//2 + 2):
        word = ''
        currword = s[:i]
        count = 1

        for j in range(i, len(s)+i,i):
            if currword == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    word += currword
                else:
                    word += str(count) + currword
                currword = s[j: j+i]
                count = 1

        sol = min(sol, len(word))
    return sol

print(solution("aabbaccc"))