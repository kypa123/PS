import heapq
def solution(scoville, K):
    if len(scoville) < 2:
        return 0
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            if scoville[0] < K:
                return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b*2))
        count += 1
    return count