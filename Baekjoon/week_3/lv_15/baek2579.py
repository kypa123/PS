N = int(input())
arr = [int(input()) for i in range(N)]

if N <= 2:
    print(sum(arr))
    exit(0)

arr2 = [arr[0], arr[0]+arr[1], max(arr[0] + arr[2], arr[1] + arr[2])]

for i in range(3, N):
    arr2.append(max(arr2[i - 2] + arr[i], arr2[i - 3] + arr[i] + arr[i - 1]))


print(arr2[-1])