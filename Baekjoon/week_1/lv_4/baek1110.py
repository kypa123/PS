N = input()
if int(N) < 10:
    A = '0'+N
else:
    A = N
orgnum = A
count = 1
while True:
    B = int(A[0])+int(A[1])
    C = A[1] + str(B)[-1]
    if C == orgnum:
        break
    else:
        A = C
        count += 1
print(count)