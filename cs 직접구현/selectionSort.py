arr = [3,7,1,15,4,2,8,10,6]
n = 0
l = len(arr)


def selectionSort(arr, n):
    midx = n
    for i in range(n+1, l):
        if arr[i] < arr[midx]:
            midx = i
    arr[n], arr[midx] = arr[midx], arr[n]
    print(arr)
    if n < l-1:
        selectionSort(arr, n+1)

selectionSort(arr, n)


print(arr)