#처음 생각했던 방법, 1을 제외하고 2 ~ 주어진 숫자 중 가장 큰 숫자 까지,
#하나하나 나눈 후 나머지가 같다면 반복문을 계속, 그렇지 않으면 다음 숫자로
#출력은 원하는 대로 나오나, 시간초과가 나서 포기
# import sys
# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for i in range(N)]
#
# for j in range(2, max(arr)+1):
#     temp = arr[0] % j
#     for val in arr:
#         if val % j != temp:
#             temp = -1
#             break
#     if temp != -1:
#         print(j, end=" ")


N = int(input())

num = sorted([int(input()) for _ in range(N)])
re_num = []

for i in range(1, N):
    re_num.append(num[i] - num[i-1])

def findGCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

GCD = re_num[0]
for idx in range(1, len(re_num)):
    GCD = findGCD(GCD, re_num[idx])


result = set()
for i in range(2, int(GCD**0.5) + 1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD // i)
result.add(GCD)
print(*sorted(list(result)))