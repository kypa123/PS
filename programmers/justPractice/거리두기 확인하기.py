def solution(places):
    answer = []
    nx = [1,-1,0,0]
    ny = [0,0,1,-1]
    mx = [2,-2,0,0]
    my = [0,0,2,-2]
    ox = [1,1,-1,-1]
    oy = [-1,1,-1,1]
    count = 1
    for place in places:
        curr = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    for k in range(4):
                        x = i + nx[k]
                        y = j + ny[k]
                        if 0 <= x < 5 and 0 <= y < 5 and place[x][y] == 'P':
                            curr = 0
                            break
                        tx = i + mx[k]
                        ty = j + my[k]
                        if 0 <= tx < 5 and 0 <= ty < 5 and place[tx][ty] == 'P':
                            if k == 0:
                                if place[tx-1][ty] != 'X':
                                    curr = 0
                                    break
                            elif k == 1:
                                if place[tx+1][ty] != 'X':
                                    curr = 0
                                    break
                            elif k == 2:
                                if place[tx][ty-1] != 'X':
                                    curr = 0
                                    break
                            elif k == 3:
                                if place[tx][ty+1] != 'X':
                                    curr = 0
                                    break
                        zx = i + ox[k]
                        zy = j + oy[k]
                        if 0 <= zx < 5 and 0 <= zy < 5 and place[zx][zy] == 'P':
                            if k == 0:
                                if place[zx-1][zy] != 'X' or place[zx][zy+1] != 'X':
                                    curr = 0
                                    break
                            elif k == 1:
                                if place[zx-1][zy] != 'X' or place[zx][zy-1] != 'X':
                                    curr = 0
                                    break
                            elif k == 2:
                                if place[zx+1][zy] != 'X' or place[zx][zy+1] != 'X':
                                    curr = 0
                                    break
                            elif k == 3:
                                if place[zx+1][zy] != 'X' or place[zx][zy-1] != 'X':
                                    curr = 0
                                    break
        answer.append(curr)
        count += 1
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))