from collections import defaultdict


def solution(numbers, hand):
    left_loc = [3, 0]
    right_loc = [3, 2]
    left = [1, 4, 7]
    right = [3, 6, 9]
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    d = defaultdict(list)
    for i in range(4):
        for j in range(3):
            d[phone[i][j]] = [i, j]
    answer = ''
    for number in numbers:
        if number in left:
            answer += 'L'
            left_loc = d[number]
        elif number in right:
            answer += 'R'
            right_loc = d[number]
        else:
            x, y = d[number]
            l = abs(left_loc[0] - x) + abs(left_loc[1] - y)
            r = abs(right_loc[0] - x) + abs(right_loc[1] - y)
            if l < r:
                answer += 'L'
                left_loc = d[number]
            elif r < l:
                answer += 'R'
                right_loc = d[number]
            else:
                if hand == 'right':
                    answer += 'R'
                    right_loc = d[number]
                else:
                    answer += 'L'
                    left_loc = d[number]
    return answer


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
