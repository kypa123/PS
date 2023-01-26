import heapq
from sys import stdin
N = int(stdin.readline())
heap = []
for _ in range(N):
    num = int(stdin.readline().strip())
    if num != 0:
        heapq.heappush(heap, (-num))
    else:
        try:
            print(-1 * heapq.heappop(heap))
        except:
            print(0)
