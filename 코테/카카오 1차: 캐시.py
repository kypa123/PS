from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cache = deque()
    answer = 0
    location = 0

    for i in range(len(cities)):
        if len(cache) < cacheSize:
            temp = cities[i].lower()
            if temp in cache:
                answer += 1
                cache.remove(temp)
                cache.append(temp)
            else:
                cache.append(cities[i].lower())
                answer += 5
        if len(cache) == cacheSize:
            location = i
            break

    for j in range(location+1, len(cities)):
        curr = cities[j].lower()
        if curr in cache:
            answer += 1
            cache.remove(curr)
            cache.append(curr)
        else:
            answer += 5
            cache.popleft()
            cache.append(curr)
    return answer