from sys import stdin
import heapq

N = int(stdin.readline())

heap = []
# 튜플, 딕셔너리 등 쌍을 이루는 값을 heap 에 push했을 시, 0번째 인덱스의 값을 기준으로 정렬하는 것을 이용.
# (절댓값, 원래값) 을 힙에 넣어 절댓값 기준으로 정렬, 출력 할때는 원래 값을 이용하도록
for _ in range(N):
    num = int(stdin.readline().strip())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))

    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)