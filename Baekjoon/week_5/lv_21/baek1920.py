N = int(input())
arr = list(map(int,(input().split())))

n = int(input())
arr2 = list(map(int,(input().split())))

arr.sort()


def func(number, start, end):
    global arr
    mid = (start+end) // 2
    if start > end:
        return 0
    if number == arr[mid]:
        return 1
    elif arr[mid] <= number:
        start = mid + 1
    else:
        end = mid - 1

    return func(number, start, end)


for val in arr2:
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    print(func(val, start, end))
