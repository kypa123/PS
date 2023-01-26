import sys
N = sys.stdin.readline()
arr = sorted(map(int, sys.stdin.readline().split()))
n = sys.stdin.readline()
arr2 = map(int, sys.stdin.readline().split())

def binary(number, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == number:
        i, j = 1, 1
        while mid-i >= start:
            if arr[mid-i] != arr[mid]:
                break
            else:
                i += 1
        while mid + j <= end:
            if arr[mid+j] != arr[mid]:
                break
            else:
                j += 1
        return i + j - 1

    elif arr[mid] < number:
        return binary(number, mid+1, end)
    elif arr[mid] > number:
        return binary(number, start, mid-1)


ans = {}
for val in arr:
    start = 0
    end = len(arr) - 1
    if val not in ans:
        ans[val] = binary(val, start, end)

print(' '.join(str(ans[x]) if x in ans else '0' for x in arr2))