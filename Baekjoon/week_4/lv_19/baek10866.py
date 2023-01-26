from collections import deque
import sys
N = int(sys.stdin.readline())
arr = deque()

for _ in range(N):
    word = sys.stdin.readline().split()
    if word[0] == "push_front":
        arr.appendleft(word[1])

    elif word[0] == "push_back":
        arr.append(word[1])

    elif word[0] == "pop_front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())

    elif word[0] == "pop_back":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())

    elif word[0] == "size":
        print(len(arr))

    elif word[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)

    elif word[0] == "front":
        if arr:
            print(arr[0])
        else:
            print(-1)

    elif word[0] == "back":
        if arr:
            print(arr[-1])
        else:
            print(-1)