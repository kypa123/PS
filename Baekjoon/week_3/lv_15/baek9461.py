arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

N = int(input())

arr2 = [int(input()) for i in range(N)]


for i in range(10, 100):
    arr.append(arr[i - 5] + arr[i - 1])


for val in arr2:
    print(arr[val-1])