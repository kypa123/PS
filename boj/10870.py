N = int(input())


fibo = [0]*(N+2)
fibo[1] = 1

if N < 2:
    print(N)
    exit(0)

for i in range(2, N+2):
    fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[N])