from collections import deque
import sys
input = sys.stdin.readline

rv = [0, 0, 1, -1, 1, -1, 1, -1]
cv = [1, -1, 0, 0, 1, -1, -1, 1]

def bfs(r, c, flag):
    global cnt
    if visited[r][c]:
        return
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        if r < 0 or c < 0 or r >= h or c >= w:
            continue
        if not visited[r][c]:
            visited[r][c] = True
            if mat[r][c]:
                if flag == 0:
                    cnt += 1
                    flag = 1
                for i in range(8):
                    nr = r + rv[i]
                    nc = c + cv[i]
                    q.append((nr, nc))

res = []
while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mat = [[] for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        mat[i] = list(map(int, input().split()))
    for i in range(h):
        for j in range(w):
            bfs(i, j, 0)
    res.append(cnt)

for r in res:
    print(r)