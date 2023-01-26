# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Point2D  # library with types used in the task
def solution(A):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)-2):
        curr = A[i]
        for left in range(i+1, len(A)-1):
            right= len(A)-1
            while left < right:
                if curr.x == A[left].x and A[left].x == A[right].x:
                    count+=1
                elif curr.y == A[left].y and A[right].y == A[left].y:
                    count += 1
                else:
                    if A[right].y == A[left].y or A[right].x == A[left].x or A[left].x == curr.x or A[left].y == curr.y:
                        right -= 1
                        continue
                    diff = (A[left].x - curr.x) / (A[left].y - curr.y)
                    thirdDiff = (A[right].x - A[left].x) / (A[right].y - A[left].y)
                    if diff == thirdDiff:
                        count += 1
                right -= 1
    return count

# Example test:   [[0, 0], [1, 1], [2, 2], [3, 3], [3, 2], [4, 2], [5, 1]]
# OK