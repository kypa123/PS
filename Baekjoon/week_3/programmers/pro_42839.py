def solution(numbers):
    arr = []
    arr2 = []
    for val in numbers:
        arr.append(val)
    temp = numbers[0]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if j == i:
                continue
            else:
                arr2.append(temp+arr[j])

    answer = 0
    return answer


N = input()
ans = solution(N)
print(ans)



# def prime_check(n):
#     if n <= 1 :
#         return False
#     for div in range(2,int(math.sqrt(n))+1):
#         if n%div == 0:
#             return False
#     return True


#함수를 사용할 수 없는 상황에, 수학에서 정해둔 공식(해당숫자의 제곱근을 나눠봤을 때 0이 아니면 소수다)
