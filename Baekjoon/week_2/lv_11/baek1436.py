N = int(input())

count = 1
num = 666
arr = [num]
a = num
while count < N:
    temp = a + 1
    if '666' in str(temp):
        if temp not in arr:
            arr.append(temp)
            count += 1
        else:
            a = temp
            continue
    else:
        a = temp

print(arr[-1])

# 복잡도 선에서 개선될 여지가 많지만, 단순하게 1씩 더해서 666이 포함되었다면 arr에 집어넣는 방법으로 해결