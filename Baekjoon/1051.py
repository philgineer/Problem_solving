import sys
input = sys.stdin.readline

def find_square(r, c):
    for diff in range(m-1-c, 0, -1):
        if graph[r][c] == graph[r][c+diff] and \
            r+diff < n and graph[r][c] == graph[r+diff][c] and \
            graph[r][c] == graph[r+diff][c+diff]:
                    return (diff + 1) ** 2
    return 1

n, m = map(int, input().split())
graph = [[-1] * m for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(m):
        graph[i][j] = int(s[j])

res = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res[i][j] = find_square(i, j)

print(max(map(max, res)))