import sys
input = sys.stdin.readline

dir_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]

def copy_mat():
    temp = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            temp[i][j] = origin[i][j]
    return temp

def make_visited():
    return [[False] * M for _ in range(N)]

def bfs(mat, visited, r, c):
    if r < 0 or r > N - 1 or c < 0 or c > M - 1 or visited[r][c]:
        return
    if not visited[r][c]:
        visited[r][c] = True
    if mat[r][c] == 0:
        mat[r][c] = 2
    for d_r, d_c in dir_list:
        bfs(r + d_r, c + d_c)

def check_result(mat):
    o = copy_mat(origin)
    v = make_visited()
    for i in range(N):
        for j in range(M):
            if m[i][j] == 2:
                bfs(m, v, i, j)


print('\n===MAT===')
for m in origin:
    print(m)
print('=========\n')