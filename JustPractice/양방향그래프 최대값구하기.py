def solution(N, A, B):
    # write your code in Python 3.6
    d = dict()
    count = 0
    for i in range(len(A)):
        d[A[i]] = d.get(A[i], [])
        d[B[i]] = d.get(B[i], [])
        d[A[i]].append(B[i])
        d[B[i]].append(A[i])
    d = dict(sorted(d.items(), key=lambda item: len(item[1]), reverse=True))
    valueDict = dict()
    for values in d:
        valueDict[values] = N
        N -= 1
    for key, val in d.items():
        for vall in val:
            count += valueDict[key] + valueDict[vall]
    count = count // 2
    return count

# Example test:   (5, [2, 2, 1, 2], [1, 3, 4, 4])
# OK
#
# Example test:   (3, [1], [3])
# OK
#
# Example test:   (4, [1, 3], [2, 4])
# OK