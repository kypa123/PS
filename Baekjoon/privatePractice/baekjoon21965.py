N = int(input())
num = list(input().split())
count = 0
for i in range(1,N):
    if num[i] == num[i-1]:
        print("NO")
        exit()
    if num[i] < num[i-1]:
        count += 1
    if count == 2:
        print("NO")
        exit()
print("YES")