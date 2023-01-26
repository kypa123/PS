from sys import stdin
import heapq

heap = []

N = int(stdin.readline())

for _ in range(N):
    num = int(stdin.readline().strip())

    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)