n = int(input())

for i in range(n):
    print(" " * i + "*" * ((n-i)*2-1))

for j in range(n-1, 0, -1):
    print(" " * (j-1) + "*" * ((n-j)*2+1))