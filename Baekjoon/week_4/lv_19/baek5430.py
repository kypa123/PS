import sys
from collections import deque

N = int(sys.stdin.readline())

for _ in range(N):
    condition = False   #R로 배열을 뒤집은 상태인가 아닌가를 판별
    breaker = False     #2중 for문 안에 error 검색코드가 있으므로 한번에 빠져나가기 위한 변수
    order = sys.stdin.readline().rstrip()
    length = int(sys.stdin.readline())

    sol = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if length == 0:
        sol = deque()
    for k in range(len(order)):
        if order[k] == "R":
            if condition:
                condition = False
            else:
                condition = True
        elif order[k] == "D":
            if len(sol) == 0:
                print("error")
                breaker = True
                break
            if condition:
                sol.pop()
            else:
                sol.popleft()
    if breaker:
        continue

    print("[", end="")
    if condition:
        for x in range(len(sol)-1, -1, -1):
            if x == 0:
                print(sol[x], end="")
                break
            print(sol[x], end=",")
    else:
        print(','.join(sol), end="")
    print("]")