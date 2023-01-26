# N = int(input())
# sol = 1
# for i in range(1, N+1):
#     sol *= i
# print(sol)
# -----for문으로
def recurs(num):
    sol = 1
    if num > 0:
        sol = num * recurs(num-1)
    return sol


print(recurs(int(input())))