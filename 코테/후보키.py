from itertools import combinations

def solution(relation):
    len_key = len(relation[0])
    candidate_key = []
    for i in range(1, len_key + 1):
        for combi in combinations(range(len_key), i):  # 후보키가 될수 있는 key들의 전체 조합
            temp = list()
            for r in relation:
                curr = [r[c] for c in combi]  # 현재 후보키 조합에 해당하는 튜플 데이터
                print(curr)
                if curr in temp:  # 유일성을 만족하지 않는 경우
                    break
                else:
                    temp.append(curr)
            else:
                for ck in candidate_key:
                    if set(ck).issubset(set(combi)):  # 최소성을 만족하지 않는 경우
                        break
                else:
                    candidate_key.append(combi)
    return len(candidate_key)


solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])

