import math


def solution(fees, records):
    answer = []
    d = dict()
    ttt = dict()
    for single in records:
        t, cn, io = single.split()
        h, m = t.split(":")
        if io == "IN":
            d[cn] = d.get(cn, 0) + int(h) * 60 + int(m)
        elif io == "OUT":
            temp = d.pop(cn)
            useTime = (int(h) * 60 + int(m)) - temp
            ttt[cn] = ttt.get(cn, 0) + useTime
    for z, x in d.items():
        useTime = 1439 - x
        ttt[z] = ttt.get(z, 0) + useTime

    for name, val in ttt.items():
        if val <= fees[0]:
            answer.append([name, fees[1]])
        else:
            finalfee = 0
            finalfee += fees[1]
            val -= fees[0]
            finalfee += math.ceil(val / fees[2]) * fees[3]
            answer.append([name, finalfee])
    answer.sort()
    answer2 = [k for i, k in answer]
    return answer2


# solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])