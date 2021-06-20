from collections import deque
import sys
input = sys.stdin.readline

def bfs(mat, temp, b_idx):
    q = deque()
    q.append(b_idx)
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if mat[nr][nc] > b_size:
                continue
            if temp[nr][nc] == 0:
                temp[nr][nc] = temp[r][c] + 1
                q.append((nr, nc))

def update_mat(mat, b_idx):
    temp = [[0] * n for _ in range(n)]
    less = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 9:
                b_idx = (i, j)
            elif mat[i][j] and mat[i][j] < b_size:
                less.append((i,j))
    return less, b_idx, temp

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 0
ate = 0
b_size = 2
b_idx = (0, 0)

# Init
less, b_idx, temp = update_mat(mat, b_idx)
bfs(mat, temp, b_idx)
print('Smaller fish:', less)
print('baby index: {}'.format(b_idx))
print('MAT')
for m in mat:
    print(m)
print('TEMP')
for t in temp:
    print(t)

while less:
    prev_idx = b_idx
    dish = []
    for fish in less:
        r, c = fish
        if temp[r][c]:
            dish.append((r, c, temp[r][c]))
    if dish:
        dish.sort(key = lambda x: (x[2], x[0], x[1]))
        print('dish:',dish)
        r, c, dist = dish[0]
        # move to the closest smaller fish
        print('Moved to {} and ate a smaller fish'.format((r, c)))
        print('Total distance increase: {}'.format(dist))
        cnt += dist
        mat[b_idx[0]][b_idx[1]] = 0
        b_idx = (r, c)
        mat[b_idx[0]][b_idx[1]] = 9
        ate += 1
        print('baby size:', b_size, 'ate:',ate)
        if ate == b_size:
            print('baby size got bigger')
            b_size += 1
            ate = 0

    less, b_idx, temp = update_mat(mat, b_idx)
    if prev_idx == b_idx:
        break
    bfs(mat, temp, b_idx)

    print('MAT')
    for m in mat:
        print(m)
    print('TEMP')
    for t in temp:
        print(t)

print('Algorithm ended.')
print('Cnt:',cnt,'baby size:', b_size)