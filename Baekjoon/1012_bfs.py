import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    if i < 0 or j < 0 or i > n - 1 or j > m - 1:
        return False
    if field[i][j] == 1:
        field[i][j] = 0
        dfs(i - 1, j)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i, j + 1)
        return True
    return False

t = int(input())
res = []
for _ in range(t):
    field = []
    r = 0
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                r += 1
    res.append(r)
for r in res:
    print(r)