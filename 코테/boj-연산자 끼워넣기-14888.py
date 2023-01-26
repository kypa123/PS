N = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

minimum = 1000000000
maximum = -1000000000

def dfs(temp, total, plus, minus, multi, div):
    global maximum, minimum
    if temp == N:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return

    if plus:
        dfs(temp + 1, total + arr[temp], plus - 1, minus, multi, div)
    if minus:
        dfs(temp + 1, total - arr[temp], plus, minus - 1, multi, div)
    if multi:
        dfs(temp + 1, total * arr[temp], plus, minus, multi - 1, div)
    if div:
        dfs(temp + 1, int(total / arr[temp]), plus, minus, multi, div - 1)


dfs(1, arr[0], arr2[0], arr2[1], arr2[2], arr2[3])
print(maximum)
print(minimum)