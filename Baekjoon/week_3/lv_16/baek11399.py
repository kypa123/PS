N = int(input())
temp = 0
ans = 0
arr = list(map(int, input().split()))
arr.sort()
for num in arr:
    temp += num
    ans += temp


print(ans)
