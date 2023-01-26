def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if j == i:
                continue
            target = phone_book[i]
            l = len(target)
            for k in range(len(phone_book[j]) - l):
                if phone_book[j][k:k+l] == target:
                    return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))