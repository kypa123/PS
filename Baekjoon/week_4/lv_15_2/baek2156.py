N = int(input())
arr = [0] * 10000
for _ in range(N):
    arr[_] = int(input())

dp = [0]*10000
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0]+arr[2], arr[2]+arr[1], dp[1])
#초기값 설정. 첫번째와 두번째까지는 단순합, 세번째부터는 max를 활용해 무엇이 더 큰지 최선의 선택으로 입력

for i in range(3, N):
    dp[i] = max(arr[i]+dp[i-2], arr[i] + arr[i-1] + dp[i-3], dp[i-1])
#현재 잔과 최선의 전 전 잔의 합, 현재잔과 이전 잔과 전전전 잔의 합, 혹은 이번잔을 패스했을 때의 값

print(max(dp))
