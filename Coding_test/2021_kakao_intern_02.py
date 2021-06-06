def search(place, i, j):
    # 상하좌우 1칸
    if (i+1 < 5 and place[i+1][j] == 'P') or \
        (i-1 >= 0 and place[i-1][j] == 'P') or \
        (j+1 < 5 and place[i][j+1] == 'P') or \
        (j-1 >=0 and place[i][j-1] =='P'):
        return 1
    # 상하좌우 2칸
    if (i+2 < 5 and place[i+2][j] == 'P'):
        if place[i+1][j] != 'X':
            return 1
    if (i-2 >= 0 and place[i-2][j] == 'P'):
        if place[i-1][j] != 'X':
            return 1
    if (j+2 < 5 and place[i][j+2] == 'P'):
        if place[i][j+1] != 'X':
            return 1
    if (j-2 >= 0 and place[i][j-2] == 'P'):
        if place[i][j-1] != 'X':
            return 1
    # 대각선
    dis = 0
    if i+1 < 5 and j+1 < 5 and place[i+1][j+1] == 'P':
        if not (place[i][j+1] == 'X' and place[i+1][j] == 'X'):
            return 1
    if i+1 < 5 and j-1 >= 0 and place[i+1][j-1] == 'P':
        if not (place[i][j-1] == 'X' and place[i+1][j] == 'X'):
            return 1
    if i-1 >= 0 and j+1 < 5 and place[i-1][j+1] == 'P':
        if not (place[i][j+1] == 'X' and place[i-1][j] == 'X'):
            return 1
    if i-1 >= 0 and j-1 >= 0 and place[i-1][j-1] == 'P':
        if not (place[i][j-1] == 'X' and place[i-1][j] == 'X'):
            return 1
    return 0

def solution(places):
    res = []
    for place in places:
        disobey = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    disobey += search(place, i, j)
        if disobey == 0:
            res.append(1)
        else:
            res.append(0)

    print(res)
    return res
p = [[
"OOOOP", 
"OXPXX", 
"XPXPX", 
"OOXOX", 
"POXXP"], 

[
"POOPX", 
"OXPXP", 
"PXXXO", 
"OXXXO", 
"OOOPP"], 

["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 

[
"PXPXP", 
"XPXPX", 
"PXPXP", 
"XPXPX", 
"PXPXP"]]
solution(p)