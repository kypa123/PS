def hanoi(n, from_p, to_p, extra_p):
    if n == 1:
        print(from_p, to_p)
        return
    hanoi(n - 1, from_p, extra_p, to_p)
    print(from_p, to_p)
    hanoi(n - 1, extra_p, to_p, from_p)


N = int(input())
count = 1
for i in range(N-1):
    count = count*2 + 1
print(count)
hanoi(N, '1', '3', '2')
