# def fibonacci(n: int, count):
#     global arr
#     if n < 2:
#         arr[count][n] += 1
#         return 1
#     else:
#         sol = fibonacci(n - 2, count) + fibonacci(n - 1, count)
#     return sol
#
#
# N = int(input())
# arr = [[0, 0] for i in range(N)]
#
# for i in range(N):
#     fibonacci(int(input()), i)
#     print(arr[i][0], arr[i][1])
# 시간제한 걸린 케이스. 일반적인 재귀적 풀이법으로는 불가능

# 10
# 01
# 11
# 12
# 23
# 35
# 58
# 8 13      순서로 0의 개수: 이전숫자의 1의 게수, 1의 개수: 이전숫자의 0과 1의 개수의 합

N = int(input())

for _ in range(N):
    arr0 = [1, 0]
    arr1 = [0, 1]
    num = int(input())
    if num > 1:
        for i in range(num - 1):
            arr0.append(arr1[-1])
            arr1.append(arr0[-2] + arr1[-1])
    print(arr0[num], arr1[num])
