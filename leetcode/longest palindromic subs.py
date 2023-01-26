from itertools import permutations


def longestPalindrome(s):
    arr = []
    for i in range(1, len(s)):
        arr += permutations(s, i)
    print(arr)


longestPalindrome("babad")