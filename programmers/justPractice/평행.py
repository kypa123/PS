def solution(dots):
    for i in range(4):
        x,y = dots[i]
        for j in range(i+1, 4):
            nx, ny = dots[j]
            if x == nx and y == ny:
                return 1
            arr = list(dots[z] for z in range(len(dots)) if z != i and z != j)
            if (ny - y)/(nx - x) == (arr[0][1] - arr[1][1])/(arr[0][0] - arr[1][0]):
                return 1
    return 0

print(solution([[1, 4], [9, 2], [3, 8], [10, 4]]))