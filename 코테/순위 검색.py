from collections import defaultdict


def solution(info, query):
    answer = []
    d = defaultdict(list)
    for i in info:
        lang, posi, exp, food, score = i.split()
        d[int(score)].append([lang, posi, exp, food])
    aaa = sorted(d.items(), key=lambda item: item[0])
    for j in query:
        cnt = 0
        lang,posi,exp,foodscore = j.split('and')
        food, score = foodscore.split()
        for a in aaa:
            if a[0] >= int(score):
                lang = lang.strip()
                posi = posi.strip()
                exp = exp.strip()
                food = food.strip()
                for tl, tp, te, tf in a[1]:
                    if lang != '-' and lang != tl:
                        continue
                    if posi != '-' and posi != tp:
                        continue
                    if exp != '-' and exp != te:
                        continue
                    if food != '-' and food != tf:
                        continue
                    cnt += 1
        answer.append(cnt)
    return answer


# solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])