A,B = map(int,input().split())
if B > 45:
    B -= 45
elif B == 45:
    B = 0
else:
    B += 15
    if A == 0:
        A = 23
    else:
        A -=1
print(A , B)