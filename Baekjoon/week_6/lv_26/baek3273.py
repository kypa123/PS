N = int(input())

arr = sorted(list(map(int,input().split())))

goal = int(input())

count = 0

a = 0
b = N-1


while a < b:
    if arr[a] + arr[b] == goal:
        count += 1
        b -= 1
    elif arr[a] + arr[b] < goal:
        a += 1
    elif arr[a] + arr[b] > goal:
        b -= 1
print(count)