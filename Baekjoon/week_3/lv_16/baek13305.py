def check(index: int, array: []):
    for j in range(index+1, len(array)):    #현재 값의 다음값부터 반복문, 만약 기름값이 현재값보다 싸면 해당 인덱스번호를 반환
        if array[j] < array[index]:
            if j == len(array)-1:
                continue                    #맨 마지막 마을의 가격이 가장 싸봤자 의미가 없음.
            else:
                return j                    #맨 마지막 마을이 아니면서 현재위치보다 싸다면 그 인덱스를 반환
    return index                            #만약 현재값보다 싼 값이 없다면 나 자신의 값을 반환


N = int(input())
distance = list(map(int, input().split()))
fuel = list(map(int, input().split()))


price = 0
curr_fuel = 0

for i in range(N):
    if i == N-1:
        break
    if curr_fuel == 0:
        curr_price = fuel[i]                #급유해야하는 상황, 남은 기름이 0일 때
        left_kilo = 0
        temp = check(i, fuel)
        if temp == i:                       #현재위치가 가장 기름이 쌈. 남은 거리만큼 전부 급유
            left_kilo += sum(distance[i:])
            price += curr_price * left_kilo
            curr_fuel = left_kilo
            break
        else:
            left_kilo += sum(distance[i:temp])   #나 다음으로 싼 곳 까지의 거리까지만 급유
            price += curr_price * left_kilo
            curr_fuel = left_kilo
            curr_fuel -= distance[i]
    else:
        curr_fuel -= distance[i]


print(price)