N= int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int, input().split())))

sol=[]
for j in range(N):
    for k in range(2):
        if j==0:
            sol.append(arr[j]+arr[j+1][k])