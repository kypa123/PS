# #메모리초과가 난 첫 시도
# N = int(input())
# arr = list(map(int, input().split()))
# dp = [[0]*N for i in range(N)]
# for i in range(N):
#     for j in range(i, N):
#         if j == 0:
#             dp[i][j] = arr[j]
#         else:
#             dp[i][j] = dp[i][j-1] + arr[j]
# sol = 0
# for val in dp:
#     if max(val) > sol:
#         sol = max(val)
# print(sol)

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))