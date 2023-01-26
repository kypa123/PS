def solution(k,arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            temp = arr[i:j]
            count = 1
            curr = 0
            while True:
                if count in temp:
                    count += 1
                else:
                    curr = count
                    break
            print(temp, curr)
            if curr != k:
                answer += 1
    return answer
print(solution(8,[8,14,20,18,11,13,6,4,5,3,7,9,1,2,16,10,19,15,12,17]))