from collections import deque
import sys
input = sys.stdin.readline

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
                    print('Island started from ({},{})'.format(r,c))
                    cnt += 1
                    flag = 1
                for i in range(8):
                    nr = r + rv[i]
                    nc = c + cv[i]
                    q.append((nr, nc))

rv = [0, 0, 1, -1, 1, -1, 1, -1]
cv = [1, -1, 0, 0, 1, -1, -1, 1]
count = []

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    mat = [[] for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        mat[i] = list(map(int, input().split()))

    print()
    print('MAT')
    for m in mat:
        print(m)

    cnt = 0
    for i in range(h):
        for j in range(w):
            bfs(i, j, 0)

    print('VISITED')
    for v in visited:
        print(v)

    count.append(cnt)
    print('CNT:',cnt)
    print()

print('RES')
for c in count:
    print(c)