arr = [i for i in range(14)]
for i in range(12):
    if i == 0:
        arr.append(12)
        continue
    arr.append(arr[-1] - 1)


def calc(alphabet):
    return arr[ord(alphabet) - 65]


def where_is_a(name):
    for i in range(1, len(name)):
        if name[i] == "A":
            continue
        else:
            return i - 1
            break


def solution(name):
    answer = 0
    if len(name) == 1:
        return calc(name)
    elif name == len(name)*"A":
        return 0
    for i in range(len(name)):
        answer += calc(name[i])
    if "A" not in name:
        answer += len(name) - 1
    elif "A" in name:
        if name[1] == "A":
            a_loc = where_is_a(name)
            answer = answer + len(name) - a_loc - 1
        else:
            answer = answer + len(name) - 1
    return answer


print(solution(input()))
