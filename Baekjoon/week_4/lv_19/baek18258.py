import sys
from collections import deque

N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    word = sys.stdin.readline().split()
    if word[0] == "push":
        arr.append(word[1])

    elif word[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())

    elif word[0] == "size":
        print(len(arr))

    elif word[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif word[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])

    elif word[0] == "back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])