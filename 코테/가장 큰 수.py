def solution(numbers):
    arr = []
    for val in numbers:
        n = str(val)
        arr.append((n, n * 4)[:4])
    arr.sort(key= lambda x: x[1], reverse=True)
    answer = ''
    for val in arr:
        answer += val[0]

    if int(answer) == 0:
        return '0'
    else:
        return answer