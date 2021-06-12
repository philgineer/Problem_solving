import sys
input = sys.stdin.readline

dir_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def move(row, col, d_cur):
    power_on = True
    d_start = d_cur
    d_cur  = (d_cur + 3) % 4
    if mat[row][col] == 0:
        mat[row][col] = 2

    while power_on:
        r0, c0 = dir_list[d_cur]
        safe_idx = row + r0 >= 0 and row + r0 < n and col + c0 >= 0 and col + c0 < m
        safe_back = row - r0 >= 0 and row - r0 < n and col - c0 >= 0 and col - c0 < m
        if safe_idx and mat[row + r0][col + c0] == 0:
            row += r0
            col += c0
            move(row, col, d_cur)
            break
        elif d_cur != d_start:
            d_cur = (d_cur + 3) % 4
        elif safe_back and mat[row - r0][col - c0] != 1:
            move(row - r0, col - c0, d_cur)
            break
        else:
            power_on = False

n, m = map(int, input().split())
r, c, d = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
clean = [[0] * m for _ in range(n)]
move(r, c, d)
res = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 2:
            res += 1
print(res)