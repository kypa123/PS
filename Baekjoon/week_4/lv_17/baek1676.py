import math

N = str(math.factorial(int(input())))
count = 0

for i in range(len(N)-1, 0, -1):
    if N[i] != '0':
        break
    count += 1
print(count)