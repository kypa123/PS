N = int(input())


for i in range(N):
    curr = i
    test = curr
    temp = str(i)
    for num in temp:
        test += int(num)
    if test == N:
        print(curr)
        exit()

print(0)