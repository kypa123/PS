N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))


def binary(start, end):
    if start > end:
        return end
    count = 0
    mid = (start+end) // 2
    for val in arr:
        count += val // mid
    if count >= M:
        return binary(mid+1, end)
    else:
        return binary(start, mid-1)


print(binary(1, max(arr)))
