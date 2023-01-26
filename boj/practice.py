N = int(input())
count = 1
for i in range(N):
    a, b = map(int,input().split())
    print(f'Case {count}:', str(a+b))
    count += 1