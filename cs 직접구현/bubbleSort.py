arr = [3,7,1,15,4,2,8,10,6]
n = len(arr)


def bubblesort(arr, n):
    curr = 0
    count = 0
    print('Round:', 10-n)
    while curr < n-1:
        if arr[curr] > arr[curr+1]:
            temp = arr[curr+1]
            arr[curr+1] = arr[curr]
            arr[curr] = temp
        print(f'{curr}차: {arr}')
        curr += 1

    if n > 1:
        bubblesort(arr, n-1)


bubblesort(arr, n)
print(arr)