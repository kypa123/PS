def solution(spell, dic):
    for i in range(len(dic)):
        flag = False
        count = 0
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                count += 1
            if count == len(spell):
                flag = True
                break
        if flag:
            return 1
    return 2


print(solution(["z", "d", "x"],["def", "dww", "dzx", "loveaw"]))